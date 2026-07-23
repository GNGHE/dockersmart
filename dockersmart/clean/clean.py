from pathlib import Path

from rich.console import Console


class Clean:

    GENERATED_FILES = [
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        ".dockerignore",
        ".env.example"
    ]


    def __init__(self, project_path="."):
        self.project_path = Path(project_path)
        self.console = Console()


    def run(self):

        removed = []

        for filename in self.GENERATED_FILES:

            file = self.project_path / filename

            if file.exists():

                file.unlink()
                removed.append(filename)


        if removed:

            self.console.print(
                "\n✔ Removed files:",
                style="green"
            )

            for file in removed:
                self.console.print(
                    f"  - {file}"
                )


        else:

            self.console.print(
                "No generated files found.",
                style="yellow"
            )