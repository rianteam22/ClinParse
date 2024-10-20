import logging
import os
from datetime import datetime
from dotenv import load_dotenv

def configure_logging():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    log_filepath = os.path.join(log_dir, log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath, mode='w'),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging initialized.")
    return log_filepath

def load_environment():
    load_dotenv()
