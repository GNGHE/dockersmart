from pathlib import Path

from rich.console import Console
from rich.table import Table

from dockersmart.inspectors.aggregator import InspectionAggregator
from dockersmart.detectors.aggregator import DetectionAggregator


class Doctor:

    def __init__(self, project_path="."):
        self.project_path = Path(project_path)
        self.console = Console()

    # -------------------------
    # File checker
    # -------------------------
    def file_exists_case_insensitive(self, filenames):

        if isinstance(filenames, str):
            filenames = [filenames]

        filenames = [name.lower() for name in filenames]

        for file in self.project_path.iterdir():

            if file.name.lower() in filenames:
                return True

        return False


    def run(self):

        inspection = InspectionAggregator(str(self.project_path)).build()
        detection = DetectionAggregator(inspection).build()

        structure = inspection.get("structure", {})
        runtime = inspection.get("runtime", {})
        services = inspection.get("services", {}).get("services", [])

        table = Table(title="Dockersmart Doctor")

        table.add_column("Check", style="cyan")
        table.add_column("Status")
        table.add_column("Details")


        # -------------------------
        # Django project
        # -------------------------

        if structure.get("manage_py"):
            table.add_row(
                "manage.py",
                "✔",
                "Found"
            )
        else:
            table.add_row(
                "manage.py",
                "✖",
                "Not found"
            )


        if structure.get("settings_path"):

            table.add_row(
                "settings.py",
                "✔",
                structure["settings_path"]
            )

        else:

            table.add_row(
                "settings.py",
                "✖",
                "Not found"
            )


        # -------------------------
        # Python
        # -------------------------

        table.add_row(
            "Python",
            "✔",
            runtime.get("python_version", "Unknown")
        )


        # -------------------------
        # Database
        # -------------------------

        table.add_row(
            "Database",
            "✔",
            detection.get("database", "Unknown")
        )


        # -------------------------
        # Server
        # -------------------------

        table.add_row(
            "Server",
            "✔",
            detection.get("server", "Unknown")
        )


        # -------------------------
        # Services
        # -------------------------

        if services:

            table.add_row(
                "Services",
                "✔",
                ", ".join(services)
            )

        else:

            table.add_row(
                "Services",
                "-",
                "None detected"
            )


        # -------------------------
        # System packages
        # -------------------------

        system = detection.get(
            "system_dependencies",
            []
        )

        if system:

            table.add_row(
                "System packages",
                "✔",
                ", ".join(system)
            )

        else:

            table.add_row(
                "System packages",
                "-",
                "None"
            )


        # -------------------------
        # Existing Docker files
        # -------------------------

        dockerfile = self.file_exists_case_insensitive(
            "Dockerfile"
        )

        compose = self.file_exists_case_insensitive(
            [
                "docker-compose.yml",
                "docker-compose.yaml"
            ]
        )


        table.add_row(
            "Dockerfile",
            "✔" if dockerfile else "-",
            "Present" if dockerfile else "Not found"
        )


        table.add_row(
            "Compose",
            "✔" if compose else "-",
            "Present" if compose else "Not found"
        )


        self.console.print(table)


        # -------------------------
        # Final status
        # -------------------------

        if structure.get("manage_py") and structure.get("settings_path"):

            self.console.print(
                "\n[bold green]✔ Project is ready to be dockerized.[/bold green]"
            )

        else:

            self.console.print(
                "\n[bold red]✖ This directory is not a valid Django project.[/bold red]"
            )