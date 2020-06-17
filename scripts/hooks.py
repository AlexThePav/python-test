import logging
from .utils import logger

class BaseTarget:
    # Initialization hooks
    def pytest_sessionstart(self, session):
        logging.info("Running sessionstart")

    def pytest_sessionfinish(self, session):
        logging.info("Running sessionfinish")
    
    # Test running hooks
    def pytest_runtest_setup(self, item):
        logging.info("Running runtest_setup")