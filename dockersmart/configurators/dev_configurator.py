from dockersmart.models.docker_configuration import DockerConfiguration
from dockersmart.configurators.base_configurator import BaseConfigurator


class DevConfigurator(BaseConfigurator):

    def build(self):

        python_version = self.get_python_version()

        return DockerConfiguration(

            mode="development",

            project_name=self.get_project_name(),

            python_version=python_version,

            base_image=f"python:{python_version}",

            working_dir=self.get_project_root(),

            command="python manage.py runserver 0.0.0.0:8000",

            database=self.get_database(),

            server=self.get_server(),

            services=self.get_services(),

            monitoring=self.get_monitoring(),

            system_dependencies=self.get_system_dependencies(),

            use_volumes=True,
            collectstatic=False,
            optimize_image=False
        )