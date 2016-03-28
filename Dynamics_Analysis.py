import lxml
from xmlutils.xml2csv import xml2csv
import pandas as pd

import xml.etree.ElementTree as ET
overdict = dict()
countNumber = 0

tree = ET.parse('me274_2015New.xml')
root = tree.getroot()
for childroot in root:
	for item in childroot:
		tempdict = dict()
		#print("zzzzzzzzzzzzzzzzzzzzzcountNumber: "+str(countNumber))
		
		
		for unknown in item:
			if 'creator' in unknown.tag:
				parent = unknown.text+'@purdue.edu'
				tempdict['poster'] = parent
				commentList = []
				commentStirng = ''
				commentDateString = ''
				parent = ''
				iden = ''
			for data in unknown:
				if 'comment_id' in data.tag:
					iden += data.text + ' '
					tempdict['id'] = iden
				elif 'comment_author_email' in data.tag:
					#print('comment_author_email: ' + data.text)
					commentStirng = commentStirng + data.text + ' '
					tempdict['commenter'] = commentStirng
				elif 'comment_date' in data.tag and 'comment_date_gmt' not in data.tag:
					commentDateString = commentDateString + data.text + ' '
					tempdict['commenter_time'] = commentDateString
					#print('comment_date: '+data.text)
				elif 'comment_parent' in data.tag:
					parent += data.text + ' '
					tempdict['parent'] = parent
		if(len(tempdict)  > 1):
			overdict[countNumber] = tempdict
			countNumber += 1
pd.DataFrame.from_dict(overdict,orient = 'index').to_csv('analysis_2015.csv')
