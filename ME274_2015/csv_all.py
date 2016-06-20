# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:07:56 2016

@author: zxy
"""

import pandas as pd
import numpy as np
import math
from itertools import combinations
import csv
node2 = dict()


data = pd.read_csv("analysis_2015.csv",low_memory=False)
for row in data.itertuples():
    poster = row[3]
    if poster not in node2:
        node1 = dict()
        node1['start'] = row[5]
        node2[poster] = node1
    else:
        if node2[poster]['start'] > row[5]:
            node2[poster]['start'] = row[5]
    initial = row[4].split(' ')
    initial.remove('')
    initial_time = row[6].split(',')
    initial_time.remove('')
    x = 0
    y = 0
    for person in initial:
        if person not in node2:
            node1 = dict()
            node1['start'] = initial_time[x]
            node2[person] = node1
        else:
            if node2[person]['start'] > initial_time[x]:
                node2[person]['start'] = initial_time[x]
        x += 1
new_node = pd.DataFrame.from_dict(node2,orient = 'index')
new_node.to_csv('node_2015.csv')
'''
node2 = dict()
edge = []
y = 0
for row in data.itertuples():
    initial = str(row[1]).split(" ")
    for person in initial:
        if person not in node2 and person != 'nan':
            node1 = dict()
            node1['start'] = row[2]
            node1['end'] = row[2]
            node2[person] = node1
        elif person in node2 and person != 'nan':
            if node2[person]['start'] > row[2]:
                node2[person]['start'] = row[2]
            if node2[person]['end'] < row[2]:
                node2[person]['end'] = row[2]
    for combos in combinations(initial,2):
        newcombos = combos + (str(row[2]),'5/14/2015 0:00',)
        edge.append(newcombos)
        
        
new_node = pd.DataFrame.from_dict(node2,orient = 'index')
new_node.to_csv('node.csv')
print()
myfile = open('connection_all.csv','w')
wr = csv.writer(myfile)
for edge_data in edge:
    
    wr.writerow(edge_data)

'''