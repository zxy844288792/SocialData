import sys,pprint

sys.path.append('../gexf')
from _gexf import Gexf, GexfImport

#test ME274_2015.gexf
f = open("ME274_2016.gexf")
gexf_import = Gexf.importXML(f)
f.close()
f = open("ME274_2016.gexf")
gexf_import2 = Gexf.importXML(f)
f.close()
print "Text gexf comparision "+ str(gexf_import == gexf_import2)

graph = gexf_import.graphs[0]

#Display node list
for node_id, node in graph.nodes.iteritems():
	print node.label
	pprint.pprint(node.getAttributes(), indent = 1, width = 1)

#Display edges list
for edgeid, edge in graph.edges.iteritems() :
	print str(graph.nodes[edge.source]) + " -> "+str(graph.nodes[edge.target])
	pprint.pprint(edge.getAttributes(), indent = 1, width = 1)

o = open("ME274_2016.gexf","w")

gexf_import.write(o)