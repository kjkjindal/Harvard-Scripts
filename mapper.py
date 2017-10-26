import csv

f1=file('Book3.csv')
f2=file('poolmap.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)

geneList=list(r1)
mapper=list(r2)

for i in range (0, len(geneList)):
	for j in range(0, len(mapper)):
		if mapper[j][1]==geneList[i][1]:
			geneList[i].append(mapper[j][0])

for i in range(0, len(geneList)):
	with open('mappedProbes2.csv','a') as helaData:
			helaWrite=csv.writer(helaData)
			helaWrite.writerow(geneList[i])