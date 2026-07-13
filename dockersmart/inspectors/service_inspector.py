class ServiceInspector:

    SERVICE_MAP = {
        "celery": "celery",
        "redis": "redis",
        "flower": "flower",
        "channels": "channels",
        "rq": "rq",
        "django-rq": "rq",
    }

    def inspect(self, dependencies: list):

        services = set()

        for dep in dependencies:
            service = self.SERVICE_MAP.get(dep)
            if service:
                services.add(service)

        return {
            "services": sorted(services)
        }