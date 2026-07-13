class ServerDetector:

    def detect(self, dependencies: list):

        if "gunicorn" in dependencies:
            return "gunicorn"

        if "uvicorn" in dependencies:
            return "uvicorn"

        if "daphne" in dependencies:
            return "daphne"

        return "wsgi"