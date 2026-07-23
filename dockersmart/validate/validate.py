from pathlib import Path

import yaml

from rich.console import Console
from rich.table import Table


class Validate:

    def __init__(self, project_path="."):
        self.project_path = Path(project_path)
        self.console = Console()


    def run(self):

        table = Table(
            title="Dockersmart Validate"
        )

        table.add_column("Check")
        table.add_column("Status")
        table.add_column("Details")


        # Dockerfile
        dockerfile = self.project_path / "Dockerfile"

        if dockerfile.exists():

            table.add_row(
                "Dockerfile",
                "✔",
                "Found"
            )

        else:

            table.add_row(
                "Dockerfile",
                "✖",
                "Missing"
            )


        # Compose

        compose = None

        for name in [
            "docker-compose.yml",
            "docker-compose.yaml"
        ]:

            file = self.project_path / name

            if file.exists():
                compose = file
                break


        if compose:

            table.add_row(
                "Compose",
                "✔",
                compose.name
            )

            self.validate_yaml(
                compose,
                table
            )

        else:

            table.add_row(
                "Compose",
                "✖",
                "Missing"
            )


        # Env

        env = self.project_path / ".env.example"

        table.add_row(
            ".env.example",
            "✔" if env.exists() else "-",
            "Found" if env.exists() else "Missing"
        )


        self.console.print(table)



    def validate_yaml(self, file, table):

        try:

            with open(file) as f:
                yaml.safe_load(f)


            table.add_row(
                "YAML syntax",
                "✔",
                "Valid"
            )


        except Exception as e:

            table.add_row(
                "YAML syntax",
                "✖",
                str(e)
            )