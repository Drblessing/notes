#!/usr/bin/env python3
import os
import pyperclip
import argparse


def convert_dot_to_dir_name(path):
    if path == "." or path == "./":
        path = os.getcwd()
        # get base path
        path = os.path.basename(path)
    elif path == ".." or path == "../":
        path = os.getcwd()
        path = os.path.dirname(path)
        path = os.path.basename(path)
    return path


def list_files(startpath):
    output_string = ""

    # Replace tilde with home directory
    if startpath[0] == "~":
        startpath = os.path.expanduser(startpath)

    fullpath = os.path.abspath(startpath)

    # Turn dot into current directory
    if startpath in [".", "./", "..", "../"]:
        startpath = convert_dot_to_dir_name(startpath)

    # Add trailing slash if not present
    if startpath[-1] != "/":
        startpath += "/"

    # Print directory name
    output_string += startpath + "\n"

    subcontents = os.listdir(fullpath)

    files = [c for c in subcontents if os.path.isfile(fullpath + os.sep + c)]
    dirs = [c for c in subcontents if os.path.isdir(fullpath + os.sep + c)]

    # Print top-level files and directories, sorted
    for f in sorted(files):
        # Add first level of indentation
        output_string += "    " + f + "\n"

    for d in sorted(dirs):
        # Add first level of indentation
        output_string += "    " + d + "/\n"

        # Get contents of subdirectory
        subcontents = os.listdir(fullpath + os.sep + d)

        # Get files and directories
        files = [
            c for c in subcontents if os.path.isfile(fullpath + os.sep + d + os.sep + c)
        ]
        dirs = [
            c for c in subcontents if os.path.isdir(fullpath + os.sep + d + os.sep + c)
        ]

        # Print files and directories, sorted
        for f in sorted(files):
            # Add second level of indentation
            output_string += "        " + f + "\n"

        for d in sorted(dirs):
            output_string += "        " + d + "/\n"

    # Remove final newline
    output_string = output_string[:-1]
    # Copy to clipboard
    pyperclip.copy(output_string)

    print(output_string)

    return output_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="List directories and subcontents 1 level down."
    )
    parser.add_argument(
        "path", type=str, help="Path to the directory", default=".", nargs="?"
    )

    args = parser.parse_args()
    list_files(args.path)
