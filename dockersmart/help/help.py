from rich.console import Console


class Help:

    def __init__(self):
        self.console = Console()


    def run(self):

        self.console.print(
"""
[bold cyan]Dockersmart CLI[/bold cyan]

Commands:

  init dev        Generate development Docker setup
  init prod       Generate production Docker setup

  doctor          Analyze Django project
  validate        Validate generated Docker files

  clean           Remove generated Docker files

  version         Display Dockersmart version

Options:

  --verbose       Show details
  --debug         Show internal data
  --dry-run       Preview without writing files
"""
        )