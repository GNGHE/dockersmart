from pathlib import Path


class EnvGenerator:

    def generate(self, config, output_path: str):

        env_content = [
            "DEBUG=1" if config.mode == "development" else "DEBUG=0",
            "SECRET_KEY=change-me",
            "ALLOWED_HOSTS=*"
        ]

        if "postgresql" in config.services:
            env_content.append("DB_ENGINE=postgresql")

        Path(output_path).write_text("\n".join(env_content))

        return output_path