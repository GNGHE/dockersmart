from pathlib import Path
from dockersmart.utils.file_finder import FileFinder


class StructureInspector:

    def __init__(self, root_path: str):
        self.finder = FileFinder(root_path)

    def _extract_project_name(self, settings_path: str) -> str:
        """
        Django structure:
        project/
            manage.py
            project/
                settings.py
        """

        if not settings_path:
            return "app"

        # ex: /path/project/portfolio/settings.py
        path = Path(settings_path)

        # project module = parent folder of settings.py
        return path.parent.name

    def inspect(self):
        manage_py = self.finder.find_files("manage.py")
        settings = self.finder.find_files("settings.py")
        wsgi = self.finder.find_files("wsgi.py")
        asgi = self.finder.find_files("asgi.py")

        settings_path = str(settings[0]) if settings else ""

        project_name = self._extract_project_name(settings_path)

        return {
            "project_root": str(self.finder.root),
            "project_name": project_name,
            "manage_py": bool(manage_py),
            "settings_path": settings_path,
            "has_wsgi": bool(wsgi),
            "has_asgi": bool(asgi)
        }