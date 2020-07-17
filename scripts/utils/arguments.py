import argparse

class ArgumentClinic:
    
    @classmethod
    def email_argument(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", action="store_true")
        args = parser.parse_args()
        return args.e