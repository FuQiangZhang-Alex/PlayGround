
import regex
import os
from XSD2TBL import *

xsd_path = XSD_CONF['path']
tbl_path = XSD_CONF['output']
xsd_files = os.popen(cmd='ls ' + xsd_path, mode='r')
name = regex.compile(pattern=r'(?<=name=").+?(?=")')
for xsd in xsd_files.readlines():
    print('########', xsd.rstrip('\n'), '#########')
    full_path = xsd_path + xsd.rstrip('\n')
    file = open(file=full_path, mode='r')
    tbl = ''
    for line in file.readlines():
        matches = name.search(line)
        if matches is not None:
            tbl += matches.captures()[0] + '\n'
    print(tbl)
