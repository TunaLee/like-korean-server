import os
from time import strftime, gmtime


def file_path(path, filename):
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(path, filename)
