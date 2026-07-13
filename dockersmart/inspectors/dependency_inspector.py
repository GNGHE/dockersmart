from dockersmart.utils.file_finder import FileFinder
from dockersmart.utils.file_reader import FileReader

class DependencyInspector:

    def __init__(self, root_path: str):
        self.finder = FileFinder(root_path)
        self.reader = FileReader()

    def inspect(self):

        deps = []

        req_files = self.finder.find_files("requirements.txt")

        for file in req_files:

            content = self.reader.read(file)

            for line in content.splitlines():
                line = line.strip()

                if line and not line.startswith("#"):
                    deps.append(line.split("==")[0])

        return {
            "dependencies": deps
        }