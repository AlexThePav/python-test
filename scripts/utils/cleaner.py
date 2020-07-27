from os import remove, walk, path
from settings import REPORTS_DIR, REPORT_FILE, REPORTS_MAX_LENGTH

def clean_reports():
    max_length = REPORTS_MAX_LENGTH
    for root, dirs, files in walk(REPORTS_DIR):
        sorted_files = sorted(files)
        if len(files) >= max_length:
            deleting_files = sorted_files[:len(files)-max_length]
            for report in deleting_files:
                remove(path.join(REPORTS_DIR, report))