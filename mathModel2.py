import csv

alpha=0.53
init=20000
newList=[]

for i in range(0, 20):
	newList.append([])
	for j in range(0,10):
		newList[i].append(((1000*j)+(i*(alpha)*(1000*j))))

for i in range(0, len(newList)):
	print newList[i]
for i in range(0, len(newList)):
	with open('test2.csv','a') as helaData:
		helaWrite=csv.writer(helaData)
		helaWrite.writerow(newList[i])