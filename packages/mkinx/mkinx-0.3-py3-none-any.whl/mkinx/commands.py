import os
import time
import sys
import threading
import socketserver
import subprocess
from pathlib import Path
from shutil import copyfile, copytree, rmtree
from http.server import SimpleHTTPRequestHandler
import getpass
import pexpect
from watchdog.observers import Observer
import warnings

from . import utils
from .conf import PORT, __VERSION__


def custom_formatwarning(msg, *args, **kwargs):
    # ignore everything except the message
    return str(msg) + "\n"


warnings.formatwarning = custom_formatwarning


@utils.suggest_path
def serve(args):
    """Start a server which will watch .md and .rst files for changes.
    If a md file changes, the Home Documentation is rebuilt. If a .rst
    file changes, the updated sphinx project is rebuilt

    Args:
        args (ArgumentParser): flags from the CLI
    """
    # Sever's parameters
    port = args.serve_port or PORT
    host = "0.0.0.0"

    # Current working directory
    dir_path = Path().absolute()
    web_dir = dir_path / "site"

    # Update routes
    utils.set_routes()

    # Offline mode
    if args.offline:
        os.environ["MKINX_OFFLINE"] = "true"
        _ = subprocess.check_output("mkdocs build > /dev/null", shell=True)
        utils.make_offline()

    class MkinxHTTPHandler(SimpleHTTPRequestHandler):
        """Class routing urls (paths) to projects (resources)
        """

        def translate_path(self, path):
            # default root -> cwd
            location = str(web_dir)
            route = location

            if len(path) != 0 and path != "/":
                for key, loc in utils.get_routes():
                    if path.startswith(key):
                        location = loc
                        path = path[len(key) :]
                        break

            if location[-1] == "/" or not path or path[0] == "/":
                route = location + path
            else:
                route = location + "/" + path

            return route.split("?")[0]

    # Serve as deamon thread
    success = False
    count = 0
    print("Waiting for server port...")
    try:
        while not success:
            try:
                httpd = socketserver.TCPServer((host, port), MkinxHTTPHandler)
                success = True
            except OSError:
                count += 1
            finally:
                if not success and count > 20:
                    s = "port {} seems occupied. Try with {} ? (y/n)"
                    if "y" in input(s.format(port, port + 1)):
                        port += 1
                        count = 0
                    else:
                        print("You can specify a custom port with mkinx serve -s")
                        return
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("Aborting.")
        return

    httpd.allow_reuse_address = True
    print("\nServing at http://{}:{}\n".format(host, port))
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()

    # Watch for changes
    event_handler = utils.MkinxFileHandler(
        patterns=["*.rst", "*.md", "*.yml", "*.yaml"]
    )
    observer = Observer()
    observer.schedule(event_handler, path=str(dir_path), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        httpd.server_close()
    observer.join()


def build(args):
    """Build the documentation for the projects specified in the CLI.
    It will do 4 different things for each project the
    user asks for (see flags):
        1. Update mkdocs's index.md file with links to project
           documentations
        2. Build these documentations
        3. Update the documentations' index.html file to add a link
           back to the home of all documentations
        4. Build mkdoc's home documentation

    Args:
        args (ArgumentParser): parsed args from an ArgumentParser
    """
    # Proceed?
    go = False

    # Current working directory
    dir_path = Path().resolve()

    # Set of all available projects in the dir
    # Projects must contain a PROJECT_MARKER file.
    all_projects = {
        m
        for m in os.listdir(dir_path)
        if os.path.isdir(m) and "source" in os.listdir(dir_path / m)
    }

    if args.all and args.projects:
        print(
            "{}Can't use both the 'projects' and 'all' flags{}".format(
                utils.colors.FAIL, utils.colors.ENDC
            )
        )
        return

    if not args.all and not args.projects:
        print(
            "{}You have to specify at least one project (or all){}".format(
                utils.colors.FAIL, utils.colors.ENDC
            )
        )
        return

    if args.force:
        go = True
        projects = (
            all_projects if args.all else all_projects.intersection(set(args.projects))
        )

    elif args.projects:
        s = "You are about to build the docs for: "
        s += "\n- {}\nContinue? (y/n) ".format("\n- ".join(args.projects))
        if "y" in input(s):
            go = True
            projects = all_projects.intersection(set(args.projects))
    elif args.all:
        s = "You're about to build the docs for ALL projects."
        s += "\nContinue? (y/n) "
        if "y" in input(s):
            go = True
            projects = all_projects

    if go:
        # Update projects links
        listed_projects = utils.get_listed_projects()

        # Don't update projects which are not listed in the Documentation's
        # Home if the -o flag was used
        if args.only_index:
            projects = listed_projects.intersection(projects)
        print("projects", projects)
        for project_to_build in projects:
            # Re-build documentation
            warnings.warn("[sphinx]")
            if args.verbose:
                os.system(
                    "cd {} && make clean && make html".format(
                        dir_path / project_to_build
                    )
                )
            else:
                os.system(
                    "cd {} && make clean && make html > /dev/null".format(
                        dir_path / project_to_build
                    )
                )

            # Add link to Documentation's Home
            utils.overwrite_view_source(project_to_build, dir_path)

            if args.verbose:
                print("\n>>>>>> Done {}\n\n\n".format(project_to_build))
        # Build Documentation
        if args.verbose:
            os.system("mkdocs build")
            print("\n\n>>>>>> Build Complete.")
        else:
            warnings.warn("[mkdocs]")
            os.system("mkdocs build > /dev/null")

        if args.offline:
            utils.make_offline()


def init(args):
    """Initialize a Home Documentation's folder

    Args:
        args (ArgumentParser): Flags from the CLI
    """
    # working directory
    dir_path = Path().absolute()

    if not args.project_name or args.project_name.find("/") >= 0:
        print(
            "{}You should specify a valid project name{}".format(
                utils.colors.FAIL, utils.colors.ENDC
            )
        )
        return

    project_path = dir_path / args.project_name

    # Create the Home Documentation's directory
    if not project_path.exists():
        project_path.mkdir()
    else:
        print(
            "{}This project already exists{}".format(
                utils.colors.FAIL, utils.colors.ENDC
            )
        )
        return

    # Directory with the Home Documentation's source code
    home_doc_path = project_path / "docs"
    home_doc_path.mkdir()
    help_doc_path = home_doc_path / "help"
    help_doc_path.mkdir()

    file_path = Path(__file__).resolve().parent

    # Add initial files
    copyfile(file_path / "index.md", home_doc_path / "index.md")
    copyfile(file_path / "How_To_Use_Mkinx.md", help_doc_path / "How_To_Use_Mkinx.md")
    copyfile(
        file_path / "Writing_Sphinx_Documentation.md",
        help_doc_path / "Writing_Sphinx_Documentation.md",
    )

    with open(file_path / "mkdocs.yml", "r") as f:
        lines = f.readlines()

    input_text = "What is your Documentation's name"
    input_text += " (it can be changed later in mkdocs.yml)?\n"
    input_text += "[Default: {} - Home Documentation]\n"

    site_name = input(input_text.format(args.project_name.capitalize()))
    if not site_name:
        site_name = "{} - Home Documentation".format(args.project_name.capitalize())

    lines[0] = "site_name: {}\n".format(site_name)

    with open(project_path / "mkdocs.yml", "w") as f:
        f.writelines(lines)

    copytree(file_path / "example_project", project_path / "example_project")
    static = project_path / "example_project" / "source"
    static /= "_static"
    if not static.exists():
        static.mkdir()

    _ = subprocess.check_output(
        "cd {} && mkinx build -F -A > /dev/null".format(args.project_name), shell=True
    )

    print(
        "\n\n",
        utils.colors.OKBLUE,
        "{}/{} created as a showcase of how mkinx works".format(
            args.project_name, "example_project"
        ),
        utils.colors.ENDC,
    )

    print(
        "\n",
        utils.colors.OKGREEN,
        "Succes!",
        utils.colors.ENDC,
        "You can now start your Docs in ./{}\n".format(args.project_name),
        utils.colors.HEADER,
        "$ cd ./{}".format(args.project_name),
        utils.colors.ENDC,
    )
    print(
        "  Start the server from within your Docs to see them \n  (default",
        "port is 8443 but you can change it with the -s flag):",
    )
    print(
        utils.colors.HEADER,
        " {} $ mkinx serve\n".format(args.project_name),
        utils.colors.ENDC,
    )


def version(args):
    if args.version:
        print(__VERSION__)


def autodoc(args):
    author = getpass.getuser()
    project = Path().resolve().name

    if "y" not in input(
        'Do you want to generate the documentation for "{}"? [y/n] :'.format(project)
    ):
        return

    child = pexpect.spawnu("sphinx-quickstart", ["./"], encoding="utf-8")
    res = child.expect(
        ["> Separate source and build directories*", "> Please enter a new root path*"]
    )
    if res == 1:
        print(
            "\n{}Error{}".format(utils.colors.FAIL, utils.colors.ENDC),
            "an existing conf.py has been found in the selected root path.",
        )
        print(
            "sphinx-quickstart will not overwrite existing Sphinx projects by itself."
        )
        child.close()
        if "y" in input(
            "\n{}Force overwriting?{} (you will lose the current".format(
                utils.colors.WARNING, utils.colors.ENDC
            )
            + " ./build/ and ./source/ folders) [y/n] : "
        ):
            _ = subprocess.check_output("mkinx clean", shell=True)
            child = pexpect.spawnu("sphinx-quickstart", ["./"], encoding="utf-8")
            child.expect("> Separate source and build directories*")
        else:
            return
    print("\n    Setting up the project...")

    windows = "y" if sys.platform in {"win32", "cygwin"} else "n"

    child.sendline("y")
    child.expect("> Name prefix*")
    child.sendline()
    child.expect("> Project name:*")
    child.sendline(project)
    child.expect("> Author name*")
    child.sendline(author)
    child.expect("> Project release*")
    child.sendline()
    child.expect("> Project language*")
    child.sendline("")
    child.expect("> Source file suffix*")
    child.sendline("")
    child.expect("> Name of your master document*")
    child.sendline("")
    child.expect("> Do you want to use the epub builder*")
    child.sendline("")
    child.expect("> autodoc: automatically insert docstrings*")
    child.sendline("y")
    child.expect("> doctest: automatically test code snippets*")
    child.sendline("")
    child.expect("> intersphinx: link between Sphinx documentation*")
    child.sendline("")
    child.expect('> todo: write "todo" entries*')
    child.sendline("")
    child.expect("> coverage: checks for documentation coverage")
    child.sendline("")
    child.expect("> imgmath: include math, rendered as PNG or SVG images*")
    child.sendline("")
    child.expect("> mathjax: include math*")
    child.sendline("")
    child.expect("> ifconfig: conditional inclusion of content*")
    child.sendline("")
    child.expect("> viewcode: include links to the source code*")
    child.sendline("")
    child.expect("> githubpages: create .nojekyll file to publish the document*")
    child.sendline("")
    child.expect("> Create Makefile*")
    child.sendline("")
    child.expect("> Create Windows command*")
    child.sendline(windows)
    child.expect("Creating file*")
    child.wait()
    child.close()

    print("    Building documentation...")

    utils.set_sphinx_config(Path() / "source" / "conf.py")

    try:
        _ = subprocess.check_output(
            "sphinx-apidoc -f -o source {} -e -M > /dev/null".format(project),
            shell=True,
        )
    except subprocess.CalledProcessError as e:
        # print(e)
        print(
            "{}Error{} ".format(utils.colors.FAIL, utils.colors.ENDC),
            "you should run `autodoc` from a project folder,",
            "with an importable project package",
        )
        print("Cleaning...", end="")
        _ = subprocess.check_output("mkinx clean", shell=True)
        print(u"\u2713")
        return

    utils.add_project_to_rst_index(Path() / "source" / "index.rst", project)
    utils.remove_project_name_from_titles(Path() / "source")

    os.remove(Path() / "source" / "modules.rst")

    index = Path().resolve().parent / "docs" / "index.md"
    if not index.exists():
        print("Error: the project could not be added to your home documentation")
        print("`mkinx autodoc` should be run from: ")
        print("    path/to/documentation/new_python_project")
    else:
        utils.add_project_to_doc_index(index, project)

    _ = subprocess.check_output(
        "cd .. && mkinx build -F -p {} > /dev/null".format(project), shell=True
    )

    print(
        u"""\n    Added configuration file source/conf.py
    Added documentation files /source/*.rst
    Added utility file ./Makefile
    {}

    {}Finished \u2713{} An initial directory structure has been created.

    You can now enhance your master file source/index.rst
    and other documentation source files.\n""".format(
            "Added utility file make.bat" if windows == "y" else "",
            utils.colors.OKGREEN,
            utils.colors.ENDC,
        )
    )


def clean(args):
    rmtree("source", ignore_errors=True)
    rmtree("build", ignore_errors=True)
    try:
        os.remove("Makefile")
    except FileNotFoundError:
        pass
    try:
        os.remove("make.bat")
    except FileNotFoundError:
        pass
