import os
import logging
import api_keys

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

# REST
ACCESS_TOKEN = api_keys.ACCESS_TOKEN
GET_USERS_URL = 'https://gorest.co.in/public-api/users'

# Logger
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'app.log')
LOGGING_LEVEL = logging.DEBUG

# Reports
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
REPORT_FILE = os.path.join(REPORTS_DIR, 'report.txt')
REPORTS_MAX_LENGTH = 10

# Email
sender_email = "pythontestreports@gmail.com"
sender_password = "pythontestpass1"
subject = "Python Auto Test Reports"