from capra.IO import IO, IOFileException
from capra.helpers.globals import CONFIG_PATH


class Config(IO):
    def __init__(self) -> None:
        super().__init__(CONFIG_PATH)
        self._config: dict[str, str | int] = {
            "host": "localhost",
            "port": 3333,
        }
        pass

    def set(self, key: str, value: str) -> None:
        self._config[key] = value
        pass

    def get(self, key: str) -> str | int:
        return self._config[key]

    def save(self) -> None:
        self._jwrite(self._config)
        pass

    def load(self) -> None:
        try:
            self._config = self._jread()
        except IOFileException:
            self._jwrite(self._config)
        pass
