import logging

from settings import LOG_FILE, LOGGING_LEVEL
from general_utils import create_file

log_file = create_file(LOG_FILE)

logging.basicConfig(filename=log_file, 
                    filemode='w', 
                    format='%(asctime)s - %(levelname)s: %(message)s', 
                    level=LOGGING_LEVEL)

