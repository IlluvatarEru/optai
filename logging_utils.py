import logging

LOGGING_ENABLED = True

logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set the logging level to INFO or any desired level

# Create a console handler and set the level to INFO or the desired level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the console handler
formatter = logging.Formatter('%(asctime)s -%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)


def log_text(text):
    if LOGGING_ENABLED:
        logging.info(text)
