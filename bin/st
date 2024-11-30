#!/Users/dbless/Github/notes/bin/.benv/bin/python
# SuperTar
# Tar/Untar a file, also adds renaming functionality to avoid naming conflicts,
# and when you don't know the output name of the file.
# Usage: untar <file> <output name>
import tarfile
import argparse
import tempfile
import os
import shutil


class SuperTar:
    TMPDIR = os.getenv("TMPDIR") or os.getenv("TMP", "/tmp")
    SUPERTAR_DIR = os.path.join(TMPDIR, "supertar")

    def parse_args(self):
        """Parse arguments"""
        parser = argparse.ArgumentParser(
            description="A python script that tars and untars files, but super."
        )

        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version="%(prog)s 1.0",
            help="Show program's version number and exit.",
        )

        parser.add_argument("file", help="The file to process")

        parser.add_argument(
            "output",
            nargs="?",
            help="The output file name",
        )

        parser.add_argument(
            "--untar",
            "-u",
            action="store_true",
            help="Untar the file",
        )

        args = parser.parse_args()

        # Default to .tgz for archiving,
        # and the name of the file for unarchiving
        if args.output is None:
            if not args.untar:
                args.output = args.file + ".tgz"
            else:
                args.output = args.file.replace(".tgz", "")

        return args

    def __init__(self):
        self.args = self.parse_args()

    def tar(self, output_filename, source_dir):
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))

    @staticmethod
    def list_files_in_tar(tar_path) -> str:
        with tarfile.open(tar_path, "r:gz") as tar:
            top_level = set()
            for name in tar.getnames():
                path_components = name.split(os.sep)
                if len(path_components) == 1:
                    top_level.add(name)
                else:
                    top_level.add(path_components[0])
            top_level = list(top_level)

            if len(top_level) > 1:
                raise Exception("Too many top-level directories")
        return top_level[0]

    def untar(self, output_filename, source_dir):
        os.makedirs(self.SUPERTAR_DIR, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=self.SUPERTAR_DIR) as tmpdirname:
            with tarfile.open(source_dir, "r:gz") as tar:
                tar.extractall(path=tmpdirname)
            # Find the file in the temp directory
            top_level = self.list_files_in_tar(source_dir)
            # Move the file to the output directory
            shutil.move(os.path.join(tmpdirname, top_level), output_filename)

    def run(self):
        if self.args.untar:
            self.untar(self.args.output, self.args.file)
        else:
            self.tar(self.args.output, self.args.file)


if __name__ == "__main__":
    SuperTar().run()
