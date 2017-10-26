import csv

f1=file('geneList.csv')
f2=file('probeSeq.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)

geneList=list(r1)
probeSeq=list(r2)
tempList=[]

for i in range(0, len(geneList)):
	for j in range(0, len(probeSeq)):
		if geneList[i][0]==probeSeq[j][0]:
			tempList.append(geneList[i])


for i in range(0, len(tempList)):
	with open('newList.csv','a') as newList:
		helaWrite=csv.writer(newList)
		helaWrite.writerow(tempList[i])


