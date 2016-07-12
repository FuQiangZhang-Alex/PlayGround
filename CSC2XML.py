#
#

import pandas as pd
import numpy
from lxml import etree


def getM(object):
    rtn = ''
    cnt = 0
    for m in dir(object):
        if cnt <= 5:
            rtn += str(m) + ', '
        else:
            cnt = 0
            rtn += '\n' + str(m)
        cnt += 1
    print(rtn)


table = pd.read_table(filepath_or_buffer='NHTSA_EDMUNDS_DATA.csv', chunksize=10)
# getM(table)
# print('table type:\t', type(table))
# print('chunk:', table.get_chunk(0).columns.base)

headers = table.get_chunk(0).columns.base[:-7]
for head in headers:
    node = etree.Element(head)
rows_cnt = 0

for chunk in table:
    # print('chunk type:\t', type(chunk))
    first_row = chunk.head(3)
    # print('first_row type:\t', type(first_row))
    #print('headers:\t', headers)
    
    row = first_row.get(headers)
    print(row)
    # print('cmplid type:\t', type(cmplid))
    # print('axes:\t', cmplid.axes)
    #print('cmplid value:\t', row.values)
    rows_cnt += 1
