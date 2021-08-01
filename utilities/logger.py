import logging
import inspect

def getLogger():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    filehandler = logging.FileHandler('logfile.log','a')
    formatter = logging.Formatter("% (asctime)s: %(levelname)s: %(name)s: %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger
