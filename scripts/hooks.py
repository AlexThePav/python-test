class BaseTarget:
    # Initialization hooks
    def pytest_sessionstart(self, session):
        print("Running sessionstart")

    def pytest_sessionfinish(self, session):
        print("Running sessionfinish")
    
    # Test running hooks
    def pytest_runtest_setup(self, item):
        print("Running runtest_setup")