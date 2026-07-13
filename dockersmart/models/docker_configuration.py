from dataclasses import dataclass, field


@dataclass
class DockerConfiguration:

    # Général
    mode: str
    project_name: str   # important pour celery/gunicorn

    # Runtime
    python_version: str
    base_image: str
    working_dir: str = "/app"

    # Application
    command: str = ""

    # Infrastructure
    database: str = "sqlite"

    # Services Docker (runtime)
    services: list = field(default_factory=list)

    # Monitoring (séparé = IMPORTANT)
    monitoring: list = field(default_factory=list)

    # System dependencies (apt packages)
    system_dependencies: list = field(default_factory=list)

    # Server type (gunicorn/uvicorn/wsgi)
    server: str = "wsgi"

    # Docker options
    use_volumes: bool = False
    collectstatic: bool = False
    optimize_image: bool = False