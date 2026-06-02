import logging
from pythonjsonlogger import jsonlogger


def configure_logging():

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger