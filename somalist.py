import csv

f1=file('atlasLocalization.csv')
f2=file('SomaEnsemble.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)

localData=list(r1)
somaList=list(r2)

for i in range(1, len(somaList)):
	for j in range (1, len(localData)):
		if somaList[i][1]==localData[j][0]:
			for k in range(1, len(localData[j])):
				somaList[i].append(localData[j][k])

for i in range(0, len(somaList)):
	with open('newListSoma.csv','a') as helaData:
		helaWrite=csv.writer(helaData)
		helaWrite.writerow(somaList[i])