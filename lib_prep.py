import csv

f1=file('geneList.csv')
f2=file('probeSeq.csv')


geneList=list(f1)
probeSeq=list(f2)

for i in range(0, len(geneList)):
	for j in range(0, len(probeSeq)):
		if geneList[i][0]==probeSeq[j][0]:
			geneList[i].append(probeSeq[j][1])

for i in range(0, len(geneList)):
	with open('newList.csv','a') as newList:
		helaWrite=csv.writer(newList)
		helaWrite.writerow(geneList[i])		


