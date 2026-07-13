from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class DockerfileGenerator:
    
    def __init__(self, template_dir: Path):
        self.env = Environment(loader=FileSystemLoader(str(template_dir)))

    def generate(self, config, output_path: str):

        template_name = "dockerfile/prod.j2" if config.mode == "production" else "dockerfile/dev.j2"

        template = self.env.get_template(template_name)

        content = template.render(
            python_version=config.python_version,
            working_dir=config.working_dir,
            command=config.command,
            system_dependencies=config.system_dependencies
        )

        Path(output_path).write_text(content)

        return output_path