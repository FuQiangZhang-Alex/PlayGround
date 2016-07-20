import pandas as pd
import regex
from CSVTools import *

csv_path = default['csv_path']
csv = pd.read_csv(csv_path, sep='\t')
subset = csv[['EPL Segment Description', 'Price Type ']]
types = []
for record in subset.values:
    pattern = regex.compile(pattern=r'Maintenance')
    description = record[0]
    price_type = record[1]
    if pattern.search(description):
        types.append(price_type)
types_unique = set(types)
for t in types_unique:
    print(t)
