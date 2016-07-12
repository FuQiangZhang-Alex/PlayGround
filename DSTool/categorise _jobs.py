
import os
import regex
import shutil
from DSTool import *

jobs_dir = conf['dir']['jobs_dir']
os.chdir(jobs_dir)


def add_path(file_name):
    return jobs_dir + '/' + file_name


files = os.listdir(jobs_dir)
files_full_path = list(map(add_path, files))
for file_full_path in files_full_path:
    if not regex.search(pattern=r'(?<=\.dsx)$', string=file_full_path):
        continue
    else:
        dsx = open(file=file_full_path, mode='r')
        category = regex.compile(r'(?<=^      Category ").+(?=")')
        for line in dsx.readlines():
            matched = category.search(line)
            if matched:
                # create directory and move/copy the dsx files into target directory
                directory = str(matched.captures()[0]).lstrip('\\\\').split('\\\\')[-1]
                if not os.access(path='Jobs', mode=os.R_OK):
                    os.mkdir(path='Jobs')
                if not os.access(path='Jobs/' + directory, mode=os.R_OK):
                    os.mkdir(path='Jobs/' + directory)
                if os.access(path=file_full_path, mode=os.R_OK):
                    shutil.copy2(src=file_full_path, dst='Jobs/' + directory)
            else:
                continue
