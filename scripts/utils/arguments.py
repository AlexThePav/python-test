import argparse

class ArgumentClinic:
    
    @classmethod
    def email_argument(cls):
        '''
        Creates argument for sending report via email
        Default argument is -e
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", action="store_true")
        args = parser.parse_args()
        return args.e