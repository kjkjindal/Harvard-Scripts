import csv

f1=file('sample.csv')
r1=csv.reader(f1)

rcaList=list(r1)
newList=[]

def findSat(i,x):
	sum=0
	for j in range(len(x)-9, len(x)):
		sum=sum+float(x[j][i])
	return sum/10

if (10>1 and 10<100):
	print 12
for i in range(0, len(rcaList[1])):
	'''sat=findSat(i,rcaList)'''
	sat=28000
	upt=0.8*sat
	lpt=0.5*sat
	
	for k in range(2, len(rcaList)):

		if (rcaList[k][i]<15000 and rcaList[k][i]<25000 ):
			print rcaList[k][i], lpt, upt

'''with open('testList.csv','a') as helaData:
	helaWrite=csv.writer(helaData)
	helaWrite.writerow(rcaList[0])

with open('testList.csv','a') as helaData:
	helaWrite=csv.writer(helaData)
	helaWrite.writerow(rcaList[1])

for i in range(0, len(rcaList)):
	with open('testList.csv','a') as helaData:
		helaWrite=csv.writer(helaData)
		helaWrite.writerow(newList[i])'''




