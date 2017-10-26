import csv

f1=file('probeSeqUnique.csv')
f2=file('geneListUniqueNew.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)

probeSeq=list(r1)
geneList=list(r2)

for i in range(0, len(geneList)):
	for  j in range(0, len(probeSeq)):
		if geneList[i][0]==probeSeq[j][0]:
			geneList[i].append(probeSeq[j][1])
			geneList[i].append(probeSeq[j][2])
			print j

for i in range(0, len(geneList)):
	with open('filteredList.csv','a') as filterList:
		filterWrite=csv.writer(filterList)
		filterWrite.writerow(geneList[i])