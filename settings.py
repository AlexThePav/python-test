import os
import logging

# REST
ACCESS_TOKEN = 'LNjOd8FPY3m33iig59BLh-iRQ2xYG7ChD6vC'
GET_USERS_URL = 'https://gorest.co.in/public-api/users'

# Logger
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'app.log')
LOGGING_LEVEL = logging.DEBUG