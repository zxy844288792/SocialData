# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:08:54 2016

@author: zxy
"""

import pandas as pd
import numpy as np
import math


data = pd.read_csv("sna_purdue_deidentified.csv",index_col = 'id',low_memory=False)

node2 = dict()
edge = dict()
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
    if(len(initial) > 1):
        x = 0
        for person in initial:
            if x > 0:    
                temp = dict()
                temp['responser'] = person
                temp['start'] = row[2]
                temp['poster'] = initial[0]
                edge[y] = temp
                y+=1
            x += 1
        
new_node = pd.DataFrame.from_dict(node2,orient = 'index')
new_node.to_csv('node.csv')

pd.DataFrame.from_dict(edge,orient = 'index').to_csv('connection.csv')


