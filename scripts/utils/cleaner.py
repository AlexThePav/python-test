from os import remove, walk, path

def clean_folder(folder, max_length):
    '''
    Only leaves last 'n' files in reports folder
    Number configurable in settings.py
    '''
    for root, dirs, files in walk(folder):
        sorted_files = sorted(files)
        if len(files) >= max_length:
            for report in sorted_files[:len(files)-max_length]:
                remove(path.join(folder, report))