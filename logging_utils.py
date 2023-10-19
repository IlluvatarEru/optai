import logging

LOGGING_ENABLED = True

# Configure the basic logging settings
logging.basicConfig(
    filename="logs.log", format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.NOTSET)  # Set the logger's level to NOTSET

# Create a console handler and set its level to NOTSET to capture all log messages
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.NOTSET)

# Create a formatter and attach it to the console handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)


def log_text(message):
    if LOGGING_ENABLED:
        logging.info(message)
