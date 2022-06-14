from os import remove
from os.path import exists
from json import load, dump


class IOFileException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IOException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IO:
    def __init__(self, path: str) -> None:
        self._path: str = path
        pass

    def _read(self) -> str:
        try:
            # Ensure config file exists.
            if not exists(self._path):
                raise IOFileException("File does not exist.")

            # Load config file.
            with open(self._path, "r") as file:
                return file.read()
        except Exception as ex:
            raise IOException(f"Unable to read file '{ex}'")

    def _write(self, data: str, mode: str = "w") -> None:
        try:
            # Write data to file.
            with open(self._path, mode) as file:
                file.write(data)
        except Exception as ex:
            raise IOException(f"Unable to write file '{ex}'")

        pass

    def _jread(self) -> dict[str, str | int]:
        # Ensure config file exists.
        if not exists(self._path):
            raise IOFileException("JSON file does not exist.")

        # Load config file.
        with open(self._path, "r") as file:
            return load(file)

    def _jwrite(self, data: dict[str, str | int]) -> None:
        try:
            # Write data to file.
            with open(self._path, "w") as file:
                dump(data, file)
        except Exception as ex:
            raise IOException(f"Unable to write JSON file '{ex}'")

        pass

    def delete(self) -> None:
        try:
            remove(self._path)
        except Exception as ex:
            raise IOException(f"Unable to delete file '{ex}'")
