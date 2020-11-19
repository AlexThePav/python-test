import os
import logging
import api_keys

from general_utils import create_folder

# REST
ACCESS_TOKEN = api_keys.ACCESS_TOKEN
GET_USERS_URL = 'https://gorest.co.in/public-api/users'

# Logger
LOGS_PATH = create_folder('logs')
LOG_FILE = os.path.join(LOGS_PATH, 'app.log')
LOGGING_LEVEL = logging.DEBUG
LOGS_MAX_LENGTH = 5

# Reports
REPORTS_PATH = create_folder('reports')
REPORT_FILE = os.path.join(REPORTS_PATH, 'report.txt')
REPORTS_MAX_LENGTH = 5


# Email
sender_email = "pythontestreports@gmail.com"
sender_password = "pythontestpass1"
subject = "Python Auto Test Reports"