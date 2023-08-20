import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    log_handler = RotatingFileHandler(
        "app.log",
        maxBytes=1024 * 1024,
        backupCount=3
    )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

    return logger
