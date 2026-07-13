class BaseConfigurator:

    def __init__(self, inspection: dict, detection: dict):
        self.inspection = inspection
        self.detection = detection

    def get_python_version(self):
        return self.inspection.get("runtime", {}).get("python_version", "3.12")

    def get_project_root(self):
        return self.inspection.get("structure", {}).get("project_root", "/app")

    def get_project_name(self):
        return self.inspection.get("structure", {}).get("project_name", "app")

    def get_services(self):
        return self.inspection.get("services", {}).get("services", [])

    def get_monitoring(self):
        return self.inspection.get("monitoring", {}).get("monitoring", [])

    def get_system_dependencies(self):
        return self.detection.get("system_dependencies", [])

    def get_database(self):
        return self.detection.get("database", "sqlite")

    def get_server(self):
        return self.detection.get("server", "wsgi")