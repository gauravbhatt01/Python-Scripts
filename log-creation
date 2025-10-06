import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

LOG_DIR = "my_logging_app/logs"
LOG_FILE = "app.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name="AppLogger"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "{asctime} - {name} - {levelname} - {message}",
            datefmt="%Y-%m-%d %H:%M:%S",
            style="{"
        )

        # Rotating file handler
        file_handler = RotatingFileHandler(LOG_PATH, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.propagate = False

    return logger

logger = setup_logger()

def main():
    logger.info("App started")
    logger.debug("Debugging details here")
    logger.warning("This is a warning!")
    logger.error("Something went wrong!")
    logger.critical("CRITICAL failure occurred")
    
if __name__ == "__main__":
    logger.info("App started")
    logger.debug("Debugging details here")
    logger.warning("This is a warning!")
    logger.error("Something went wrong!")
    logger.critical("CRITICAL failure occurred")
    main()
	
