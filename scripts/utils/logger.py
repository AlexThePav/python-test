import logging
import os

from datetime import datetime

from settings import LOG_FILE, LOGGING_LEVEL
from general_utils import FILE_TIMESTAMP, create_file

log_file = create_file(LOG_FILE)

logging.basicConfig(filename=log_file, 
                    filemode='w', 
                    format='%(asctime)s - %(levelname)s: %(message)s', 
                    level=LOGGING_LEVEL)

