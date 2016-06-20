import lxml
from xmlutils.xml2csv import xml2csv
import pandas as pd
import numpy as np
import math

import xml.etree.ElementTree as ET
overdict = dict()
countNumber = 0

tree = ET.parse('me274_2015New.xml')
root = tree.getroot()
for childroot in root:

	for item in childroot:
		'''
		Each item is a thread in the blog
		'''
		tempdict = dict()	

		for unknown in item:
			'''
			Each unkown is the information in the thread	
			'''
			if 'post_date' in unknown.tag and 'gmt' not in unknown.tag:
					tempdict['post_date'] = unknown.text
			if 'creator' in unknown.tag:
				parent = unknown.text+'@purdue.edu'
				tempdict['poster'] = parent
				commentList = []
				commentStirng = ''
				commentDateString = ''
				parent = ''
				iden = ''
			for data in unknown:
				'''
				Each data is the information related to the comment
				'''
				if 'comment_id' in data.tag:
					iden += data.text + ' '
					tempdict['id'] = iden
				elif 'comment_author_email' in data.tag:
					#print('comment_author_email: ' + data.text)
					commentStirng = commentStirng + data.text + ' '
					tempdict['commenter'] = commentStirng
				elif 'comment_date' in data.tag and 'comment_date_gmt' not in data.tag:
					commentDateString = commentDateString + data.text + ','
					tempdict['commenter_time'] = commentDateString
					#print('comment_date: '+data.text)
				elif 'comment_parent' in data.tag:
					parent += data.text + ' '
					tempdict['parent'] = parent
		if(len(tempdict)  > 2):
			overdict[countNumber] = tempdict
			countNumber += 1
full = pd.DataFrame.from_dict(overdict,orient = 'index')

node2 = dict()
for row in full.itertuples():
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
new_node.to_csv('node_2015_2.csv')


