from pathlib import Path
from dockersmart.utils.constants import IGNORED_DIRS

class FileFinder:

    def __init__(self, root_path: str):
        self.root = Path(root_path)

    #---------------------------
    # Scan project safely
    #---------------------------
    def find_files(self, filename: Path):
        matches = []
        for path in self.root.rglob(filename):
            if any(ignored in path.parts for ignored in IGNORED_DIRS):
                continue
            matches.append(path)
        return matches