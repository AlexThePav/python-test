class TestStatus:
    """Class for getting and setting test status"""
    def __init__(self, name='', outcome='', duration=None):
        self.name = name
        self.outcome = outcome
        self.duration = duration
    
    def __repr__(self):
        return f'{self.outcome}: {self.name}, duration: {str(self.duration)[:4]}\n'