class DatabaseDetector:

    def detect(self, dependencies: list):

        if "psycopg2" in dependencies or "psycopg2-binary" in dependencies:
            return "postgresql"

        if "mysqlclient" in dependencies or "mysql" in dependencies:
            return "mysql"

        return "sqlite"