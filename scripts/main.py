from datetime import datetime
from settings import REPORTS_MAX_LENGTH, REPORTS_PATH, LOGS_PATH, LOGS_MAX_LENGTH
import pytest
import argparse
import logging

from .utils import logger
from .hooks import BaseTarget
from .utils.arguments import ArgumentClinic
from .utils.emails import UnladenSwallow
from .utils.cleaner import clean_folder

def get_pytest_args():
    pytest_args = []
    pytest_args.append('-vs')
    pytest_args.append('./tests')
    return pytest_args

def main():
    my_plugin = BaseTarget()
    
    main_start_time = datetime.now()
    pytest.main(get_pytest_args(), plugins=[my_plugin])
    main_done_time = datetime.now() - main_start_time

    with open(my_plugin.report_file, "a") as f:
        f.write("\nRun time: " + str(main_done_time))

    if ArgumentClinic.email_argument():
        logging.info("Sending report email...")
        print("Sending report email...")
        UnladenSwallow.send_report(my_plugin.report_file, "alexandrupavilcu@gmail.com")
        logging.info("Report email sent!")
        print("Report email sent!")
    else:
        logging.info("Done. Please see reports folder")
        print("Done. Please see reports folder")
    
    clean_folder(REPORTS_PATH, REPORTS_MAX_LENGTH)
    clean_folder(LOGS_PATH, LOGS_MAX_LENGTH)
