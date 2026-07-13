from dockersmart.utils.file_finder import FileFinder
from dockersmart.utils.file_reader import FileReader


class RuntimeInspector:

    def __init__(self, root_path: str):
        self.finder = FileFinder(root_path)
        self.reader = FileReader()

    def inspect(self):
        pyproject = self.finder.find_files("pyproject.toml")
        runtime = self.finder.find_files("runtime.txt")
        version = "3.12"

        if runtime:
            content = self.reader.read(runtime[0])
            version = content.strip()

        return {
            "python_version": version
        }