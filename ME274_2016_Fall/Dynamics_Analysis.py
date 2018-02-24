'''
This script is used to extract data we need from the xml file
'''
import lxml
from xmlutils.xml2csv import xml2csv
import pandas as pd

import xml.etree.ElementTree as ET
overdict = dict()
countNumber = 0

tree = ET.parse('me274_2016FNew.xml')
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
pd.DataFrame.from_dict(overdict,orient = 'index').to_csv('analysis_2016.csv')
