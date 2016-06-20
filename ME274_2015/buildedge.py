import pandas as pd
import numpy as np
import math
from itertools import combinations
import csv

directmap = dict()
overdict = dict()
count = 0

data = pd.read_csv("analysis_2015_new.csv",low_memory=False)
for row in data.itertuples():
 	tempdict = dict()
 	poster = row[3]
 	commenter = row[4]
 	comment_id = row[7]
 	parent = row[2]
 	current = row[6]
 	directmap[comment_id] = commenter
 	if parent == 0:
 		tempdict['commenter'] = commenter
 		tempdict['poster'] = poster
 		tempdict['time'] = current
 	else:
 		tempdict['commenter'] = commenter
 		tempdict['poster'] = directmap[parent]
 		tempdict['time'] = current
 	overdict[count] = tempdict
 	count += 1
 
pd.DataFrame.from_dict(overdict,orient = 'index').to_csv('edge_2015_new.csv')