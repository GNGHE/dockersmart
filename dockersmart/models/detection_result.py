from dataclasses import dataclass, field

@dataclass
class DetectionResult:
    database: str = "sqlite"
    server: str = "wsgi"
    system_dependencies: list = field(default_factory=list)