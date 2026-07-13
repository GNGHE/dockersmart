from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class ComposeGenerator:

    def __init__(self, template_dir: Path):
        self.env = Environment(loader=FileSystemLoader(str(template_dir)))

    def generate(self, config, output_path: str):

        template_name = "compose/prod.j2" if config.mode == "production" else "compose/dev.j2"

        template = self.env.get_template(template_name)

        content = template.render(
            command=config.command,
            services=config.services,
            monitoring=config.monitoring,
            database=config.database,
            project_name=config.project_name
        )

        Path(output_path).write_text(content)

        return output_path