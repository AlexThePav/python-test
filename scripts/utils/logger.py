import logging
import os

from settings import LOG_FILE, LOGGING_LEVEL

logging.basicConfig(filename=LOG_FILE, 
                    filemode='w', 
                    format='%(asctime)s - %(levelname)s: %(message)s', 
                    level=LOGGING_LEVEL)

