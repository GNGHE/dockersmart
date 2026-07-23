from rich.console import Console


VERSION = "0.1.2"


class Version:

    def __init__(self):
        self.console = Console()


    def run(self):

        self.console.print(
            f"Dockersmart version {VERSION}",
            style="green"
        )