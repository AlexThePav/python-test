class TestStatus:
    """Class for getting and setting test status"""
    def __init__(self, name='', outcome='', duration=None, error=None):
        self.name = name
        self.outcome = outcome
        self.duration = duration
        self.error = error
    
    def __repr__(self):
        representation = f'\n{self.outcome}: {self.name}, duration: {str(self.duration)[:4]}'
        if self.error:
            representation += f'\n===\n{self.error}\n==='
        return representation
    
    def set_error(self, error_message=None):
        if "AssertionError: " in error_message:
            self.error = error_message.split("AssertionError: ")[1].split("\n")[0]
        else:
            self.error = error_message
