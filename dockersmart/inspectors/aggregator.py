from dockersmart.inspectors.structure_inspector import StructureInspector
from dockersmart.inspectors.dependency_inspector import DependencyInspector
from dockersmart.inspectors.runtime_inspector import RuntimeInspector
from dockersmart.inspectors.service_inspector import ServiceInspector


class InspectionAggregator:

    def __init__(self, root_path: str):
        self.root_path = root_path

    def build(self):

        structure = StructureInspector(self.root_path).inspect()
        dependencies = DependencyInspector(self.root_path).inspect()
        runtime = RuntimeInspector(self.root_path).inspect()

        services = ServiceInspector().inspect(
            dependencies["dependencies"]
        )

        return {
            "structure": structure,
            "dependencies": dependencies,
            "runtime": runtime,
            "services": services
        }