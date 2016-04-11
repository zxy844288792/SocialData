import pandas as pd
import numpy as np
import math
from itertools import combinations
import csv
node2 = dict()


data = pd.read_csv("analysis_2015_new.csv", low_memory = False)
for row in data.itertuples():
    poster = row[3]
    if poster not in node2:
        node1 = dict()
        node1['start'] = row[5]
        node2[poster] = node1
    else:
        if node2[poster]['start'] > row[5]:
            node2[poster]['start'] = row[5]

    commenter = row[4]
    comTime = row[6]

    if commenter not in node2:
            node1 = dict()
            node1['start'] = comTime
            node2[commenter] = node1
    else:
        if node2[commenter]['start'] > comTime:
            node2[commenter]['start'] = comTime

new_node = pd.DataFrame.from_dict(node2,orient = 'index')
new_node.to_csv('node_2015_new.csv')
            
    
