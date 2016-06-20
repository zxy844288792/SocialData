'''
This file is used to anonymous some information
'''

from xml.dom import minidom
import pandas as pd

fileobj =  open('me274basicmechanicsii.wordpress.2016-05-09.xml')
'''
The new file which delete identity information
'''
fileobj2 = open('me274_2016New.xml','w')
NameMap = dict()
x = 0
for line in fileobj:
	if('wp:author_email') in line:
		name = line.split('wp:author_email')[1].split('>')[1].split('<')[0]
		if name not in NameMap:
			AnnName = str(x)+'@purdue.edu'
			NameMap[name] = AnnName
			x += 1
		else:
			AnnName = NameMap[name]
		newline = line.replace(name,AnnName)
		newline = newline.replace(name.replace('@purdue.edu',''),AnnName.replace('@purdue.edu',''))
		fileobj2.write(newline)
	elif("wp:comment_author_email") in line:
		name = line.split('>')[1].split('<')[0]
		if name not in NameMap:
			AnnName = str(x)+'@purdue.edu'
			NameMap[name] = AnnName
			x += 1
		else:
			AnnName = NameMap[name]
		newline = line.replace(name,AnnName)
		fileobj2.write(newline)
	elif("wp:comment_author") in line and 'CDATA' in line:
		name = line.split('comment_author')[1].split('CDATA[')[1].split(']')[0]+ '@purdue.edu'
		print(name)
		fileobj2.write(line)
		sss=1
	elif "dc:creator" in line:
		name = line.split('<dc:creator>')[1].split('CDATA[')[1].split(']')[0]+ '@purdue.edu'
		
		if name not in NameMap:
			AnnName = str(x)+'@purdue.edu'
			NameMap[name] = AnnName
			x += 1
		else:
			AnnName = NameMap[name]
		newline = line.replace(name,AnnName)
		newline = newline.replace(name.replace('@purdue.edu',''),AnnName.replace('@purdue.edu',''))
		fileobj2.write(newline)
	else:
		fileobj2.write(line)
pd.DataFrame.from_dict(NameMap,orient = 'index').to_csv('NameMap_2016.csv')