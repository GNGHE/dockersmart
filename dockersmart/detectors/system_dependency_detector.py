class SystemDependencyDetector:

    RULES = {
        "psycopg2": ["gcc", "libpq-dev"],
        "pillow": ["libjpeg-dev", "zlib1g-dev"],
        "mysqlclient": ["default-libmysqlclient-dev"],
    }

    def detect(self, dependencies: list):

        system_deps = []

        for dep in dependencies:

            if dep in self.RULES:
                system_deps.extend(self.RULES[dep])

        return sorted(set(system_deps))