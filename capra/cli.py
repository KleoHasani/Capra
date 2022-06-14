from capra.Application import Application, InvalidInputException
from capra.globals import OutType
from capra.io import output, done


def bootstrap() -> None:
    try:
        app: Application = Application()
        app.start()
    except InvalidInputException as ix:
        output(ix, OutType.ERROR)
    except Exception as ex:
        output(ex)

    done()
    pass
