import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'app.log')
LOGGING_LEVEL = logging.DEBUG

logging.basicConfig(filename=LOG_FILE, 
                    filemode='w', 
                    format='%(asctime)s - %(levelname)s: %(message)s', 
                    level=LOGGING_LEVEL)

