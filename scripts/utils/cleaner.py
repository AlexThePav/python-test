from os import remove, walk, path
from settings import REPORTS_DIR, REPORT_FILE, REPORTS_MAX_LENGTH

def clean_reports():
    '''
    Only leaves last 'n' files in reports folder
    Number configurable in settings.py
    '''
    for root, dirs, files in walk(REPORTS_DIR):
        sorted_files = sorted(files)
        if len(files) >= REPORTS_MAX_LENGTH:
            for report in sorted_files[:len(files)-REPORTS_MAX_LENGTH]:
                remove(path.join(REPORTS_DIR, report))