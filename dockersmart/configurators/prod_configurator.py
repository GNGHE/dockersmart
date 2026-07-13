from dockersmart.models.docker_configuration import DockerConfiguration
from dockersmart.configurators.base_configurator import BaseConfigurator


class ProdConfigurator(BaseConfigurator):

    def build(self):

        python_version = self.get_python_version()

        project_name = self.get_project_name()

        return DockerConfiguration(

            mode="production",

            project_name=project_name,

            python_version=python_version,

            base_image=f"python:{python_version}-slim",

            working_dir=self.get_project_root(),

            command=f"gunicorn {project_name}.wsgi:application --bind 0.0.0.0:8000",

            database=self.get_database(),

            server=self.get_server(),

            services=self.get_services(),

            monitoring=self.get_monitoring(),

            system_dependencies=self.get_system_dependencies(),

            use_volumes=False,
            collectstatic=True,
            optimize_image=True
        )