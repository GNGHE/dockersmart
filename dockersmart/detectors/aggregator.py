from dockersmart.detectors.database_detector import DatabaseDetector
from dockersmart.detectors.server_detector import ServerDetector
from dockersmart.detectors.system_dependency_detector import SystemDependencyDetector


class DetectionAggregator:

    def __init__(self, inspection_result: dict):
        self.dependencies = inspection_result.get("dependencies", {}).get("dependencies", [])

    def build(self):

        database = DatabaseDetector().detect(self.dependencies)
        server = ServerDetector().detect(self.dependencies)
        system_deps = SystemDependencyDetector().detect(self.dependencies)

        return {
            "database": database,
            "server": server,
            "system_dependencies": system_deps
        }