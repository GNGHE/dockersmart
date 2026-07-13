from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class DockerignoreGenerator:

    def __init__(self, template_dir: Path):
        self.env = Environment(loader=FileSystemLoader(str(template_dir)))

    def generate(self, output_path: str):

        template = self.env.get_template("dockerignore/default.j2")

        content = template.render()

        Path(output_path).write_text(content)

        return output_path