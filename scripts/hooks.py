import logging
from .utils import logger

class BaseTarget:
    # Initialization hooks
    def pytest_sessionstart(self, session):
        logging.debug("Running sessionstart")

    def pytest_sessionfinish(self, session):
        logging.debug("Running sessionfinish")
    
    # Test running hooks
    def pytest_runtest_setup(self, item):
        logging.debug("Running runtest_setup")