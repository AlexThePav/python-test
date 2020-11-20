import pytest
import logging
import os

from .utils.status import TestStatus
from settings import REPORT_FILE
from general_utils import create_file

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
        self.report_file = create_file(REPORT_FILE)
        
        with open(self.report_file, "a") as f:
            f.write("Test report:\n")
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
            if rep.outcome == "failed":
                error_message = test_status.set_error(str(rep.longrepr))
            self.test_status_list.append(str(test_status))
