from capra.IO import IO
from capra.helpers.globals import LOG_PATH
from time import strftime, localtime, time as ctime


class Log(IO):
    def __init__(self) -> None:
        super().__init__(LOG_PATH)

    def write(self, err: str) -> None:
        local_time: str = strftime("%D %T", localtime(ctime()))
        self._write(f"{local_time} >> {err}\n", "a")
        pass
