import argparse
from pathlib import Path

from rich.console import Console

from dockersmart.inspectors.aggregator import InspectionAggregator
from dockersmart.detectors.aggregator import DetectionAggregator
from dockersmart.configurators.dev_configurator import DevConfigurator
from dockersmart.configurators.prod_configurator import ProdConfigurator
from dockersmart.generators.dockerfile_generator import DockerfileGenerator
from dockersmart.generators.compose_generator import ComposeGenerator
from dockersmart.generators.dockerignore_generator import DockerignoreGenerator
from dockersmart.generators.env_generator import EnvGenerator

from dockersmart.doctor.doctor import Doctor
from dockersmart.validate.validate import Validate
from dockersmart.clean.clean import Clean
from dockersmart.help.help import Help
from dockersmart.version.version import Version


BASE_DIR = Path(__file__).resolve().parents[1]
console = Console()


class CLI:

    def run(self):

        parser = argparse.ArgumentParser(description="Dockersmart CLI")


        parser.add_argument("command", choices=["init", "doctor", "clean", "version", "validate", "help"])

        parser.add_argument("mode", nargs="?", choices=["dev", "prod"])

        parser.add_argument("--verbose", action="store_true")
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--debug", action="store_true")

        args = parser.parse_args()
        
        
        # -------------------------
        # DOCTOR
        # -------------------------
        if args.command == "doctor":
            Doctor(".").run()
            return
        
        
        if args.command == "doctor":
            Doctor(".").run()
            return


        if args.command == "clean":
            Clean(".").run()
            return


        if args.command == "version":
            Version().run()
            return


        if args.command == "validate":
            Validate(".").run()
            return


        if args.command == "help":
            Help().run()
            return

        # -------------------------
        # VALIDATION
        # -------------------------
        if args.command != "init":
            console.print("❌ Unknown command. Use: init", style="red")
            return

        if args.mode not in ["dev", "prod"]:
            console.print("❌ Mode must be dev or prod", style="red")
            return

        # -------------------------
        # STEP 1 - INSPECTION
        # -------------------------
        if args.verbose:
            console.print("\n🔍 Inspecting project...", style="cyan")

        inspection = InspectionAggregator(".").build()

        if args.debug:
            console.print(inspection)

        # -------------------------
        # STEP 2 - DETECTION
        # -------------------------
        if args.verbose:
            console.print("⚙️ Detecting services...", style="cyan")

        detection = DetectionAggregator(inspection).build()

        if args.debug:
            console.print(detection)

        # -------------------------
        # STEP 3 - CONFIGURATION
        # -------------------------
        if args.verbose:
            console.print("🧠 Building configuration...", style="cyan")

        if args.mode == "dev":
            configurator = DevConfigurator(inspection, detection)
        else:
            configurator = ProdConfigurator(inspection, detection)

        config = configurator.build()

        # -------------------------
        # STEP 4 - GENERATION
        # -------------------------
        if args.verbose:
            console.print("🐳 Generating Docker files...", style="cyan")

        tasks = [
            "Dockerfile",
            "docker-compose.yml",
            ".dockerignore",
            ".env.example"
        ]

        if not args.dry_run:

            if args.verbose:
                console.print("  • Dockerfile")

            DockerfileGenerator(BASE_DIR / "templates").generate(
                config,
                "Dockerfile"
            )

            if args.verbose:
                console.print("  • docker-compose.yml")

            ComposeGenerator(BASE_DIR / "templates").generate(
                config,
                "docker-compose.yml"
            )

            if args.verbose:
                console.print("  • .dockerignore")

            DockerignoreGenerator(BASE_DIR / "templates").generate(
                ".dockerignore"
            )

            if args.verbose:
                console.print("  • .env.example")

            EnvGenerator().generate(
                config,
                ".env.example"
            )
        else:
            console.print("\n🧪 DRY RUN MODE - No files written", style="yellow")
            console.print(tasks)

        # -------------------------
        # DONE
        # -------------------------
        console.print("\n✔ Docker setup generated successfully", style="green")


def main():
    CLI().run()