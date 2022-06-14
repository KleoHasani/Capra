from capra.Application import Application, InputException
from capra.IO import IOException
from capra.Log import Log
from capra.helpers.globals import OutType
from capra.helpers.printer import output, done


def bootstrap() -> None:
    try:
        logger: Log = Log()
        app: Application = Application()
        app.start()

    except InputException as ix:
        output(ix)

    except IOException as iox:
        output(iox, OutType.ERROR)
        logger.write(iox)

    except Exception as ex:
        output(ex, OutType.ERROR)
        logger.write(ex)

    done()
    pass
