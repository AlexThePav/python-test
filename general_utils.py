import os

from datetime import datetime


BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

FILE_TIMESTAMP = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

def create_folder(dir_name):
    desired_path = os.path.join(BASE_DIR, dir_name)
    try:
        os.mkdir(desired_path)
    except FileExistsError:
        pass
    return desired_path

def create_file(file_type):
    file_name = os.path.splitext(file_type)[0]
    file_ext = os.path.splitext(file_type)[1]
    created_file = file_name + " " + FILE_TIMESTAMP + file_ext
    return created_file