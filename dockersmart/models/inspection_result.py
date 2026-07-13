from dataclasses import dataclass, field

@dataclass
class InspectionResult:
    structure: dict = field(default_factory=dict)
    dependencies: dict = field(default_factory=dict)
    runtime: dict = field(default_factory=dict)
    services: dict = field(default_factory=dict)