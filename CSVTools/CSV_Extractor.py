import pandas as pd
import regex
from CSVTools import *

csv_path = default['csv_path']
csv = pd.read_csv(csv_path, sep='\t')
subset = csv[[0, 8, 9, 10, 11]]
types = []
for record in subset.values:
    pattern = regex.compile(pattern=r'Maintenance')
    description = record[0]
    if pattern.search(description):
        types.append(record)
# types_unique = set(types)
for t in types:
    print(t, type(t[4]))
