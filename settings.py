import os
import logging
import api_keys

# REST
ACCESS_TOKEN = api_keys.ACCESS_TOKEN
GET_USERS_URL = 'https://gorest.co.in/public-api/users'

# Logger
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'app.log')
LOGGING_LEVEL = logging.DEBUG