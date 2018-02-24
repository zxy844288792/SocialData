import csv

##Open the original file first
with open('Statistics2015Fall.csv', 'rb') as old_csv:
	csv_reader = csv.reader(old_csv)
	with open('closs2015Fall.csv', 'wb') as new_csv: ##Create a new csv
		csv_writer = csv.writer(new_csv)
		for i, row in enumerate(csv_reader):
			if i != 0:
				##Normalization of Closeness Centrality
				##37 is the total nodes number
				row.append(float(row[2]) * float(37 - 1)) 
				##Normalization of Betweenness Centrality
				row.append(float(row[3])/float((37 - 1 )*(37 - 2) / 2))
				csv_writer.writerow(row)
