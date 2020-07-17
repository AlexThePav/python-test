import pytest
import logging
import os
from datetime import datetime

from .utils import logger
from .status import TestStatus
from settings import REPORT_FILE

class BaseTarget:
    def __init__(self):
        self.report_file_name = os.path.splitext(REPORT_FILE)[0]
        self.report_file_extension = os.path.splitext(REPORT_FILE)[1]
        self.test_status_list = []
        self.report_file = None
    

    # Initialization hooks
    def pytest_sessionstart(self, session):
        logging.info("Running sessionstart")

    def pytest_sessionfinish(self, session):
        logging.info("Running sessionfinish")
        self.report_file = self.report_file_name + " " + str(datetime.now()) + self.report_file_extension
        
        with open(self.report_file, "a") as f:
            f.write("Test report:\n\n")
            for test_status in self.test_status_list:
                f.write(test_status)
    
    # Test running hooks
    def pytest_runtest_setup(self, item):
        logging.info("Running runtest_setup")
    
    # Collection hooks
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == "call":
            test_status = TestStatus(item.name, rep.outcome, rep.duration)
            self.test_status_list.append(str(test_status))
