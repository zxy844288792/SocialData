from _gexf import *
import pandas as pd
from dateutil.parser import parse


blogdata = Gexf("xingyu zhou","ME274_2015")
graph = blogdata.addGraph('directed','dynamic','graph','dateTime')
fileobj = pd.read_csv('node_2015.csv')
for row in fileobj.iterrows():
	start = str(parse(row[1][1]))	
	start = start.split()[0] + 'T' + start.split()[1]
	#start = start.split()[0]
	#end = end.split()[0] + 'T' + end.split()[1]
	graph.addNode(row[1][0],row[1][0],start = start,r='78',g='23',b='232')

fileobj = pd.read_csv('edge_2015.csv')
x = 0
for row in fileobj.iterrows():
	start = str(parse(row[1][3]))
	start = start.split()[0] + 'T' + start.split()[1]
	graph.addEdge(x,row[1][1],row[1][2],start =start)
	x += 1


output_file=open("ME274_2015.gexf","w")
blogdata.write(output_file)
