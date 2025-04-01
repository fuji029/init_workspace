import sys
import subprocess
from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-project", required=True,
                    help="name of the project you are trying to make")
parser.add_argument("-path", required=False, default=".",
                    help="(option) path of the project")
parser.add_argument("-version", required=True, help="version of Python")
parser.add_argument("-directories", default="../default_directories.txt",
                    help="path to default directory names' file")
args = parser.parse_args()


def create_directory():

    def directories():
        with open(args.directories, "r") as f:
            data = f.read().rstrip().split("\n")
        return data

    path = Path(args.path)
    path_str = str(path.absolute())
    project_name = args.project
    res = subprocess.run(["uv", "init", project_name], cwd=path_str)
    if res.returncode != 0:
        print("Error! Cannot create your project!")
        sys.exit(1)

    res = subprocess.run(["rm", "*.py"], cwd=f"{path_str}/{project_name}")
    if res.returncode != 0:
        print("Error! Cannot remove .py files in your project directory!")
        sys.exit(1)

    path = path / project_name
    for name in directories():
        path.mkdir(name)


def main():
    create_directory()
    return 0


if __name__ == "main":
    main()
