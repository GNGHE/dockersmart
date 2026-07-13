from pathlib import Path


class FileReader:

    def read(self, file_path: Path):
        try:
            return file_path.read_text(encoding="utf-8")
        except Exception:
            return ""

    # -------------------------
    # read lines
    # -------------------------
    def read_lines(self, file_path: Path):
        content = self.read(file_path)
        return content.splitlines()