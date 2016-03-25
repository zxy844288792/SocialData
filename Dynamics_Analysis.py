import lxml
from xmlutils.xml2csv import xml2csv

import xml.etree.ElementTree as ET
overdict = dict()

tree = ET.parse('me274_2015New.xml')
root = tree.getroot()
for childroot in root:
	for item in childroot:
		for unknown in item:
			if 'creator' in unknown.tag:
				parent = unknown.text+'@purdue.edu'
				commentList = []
				commentStirng = ''
			for data in unknown:
				if 'comment_id' in data.tag:
					print('comment_id: '+data.text)
				elif 'comment_author_email' in data.tag:
					#print('comment_author_email: ' + data.text)
					commentStirng = commentStirng + data.text + ' '
				elif 'comment_date' in data.tag and 'comment_date_gmt' not in data.tag:
					print('comment_date: '+data.text)
				elif 'comment_parent' in data.tag:
					print('comment_parent: '+data.text)