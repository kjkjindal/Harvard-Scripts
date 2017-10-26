import csv

f1=file('final.csv')
f2=file('initial.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)

final=list(r1)
initial=list(r2)
newList=[]
c=0

for i in range(0, len(initial)):
	for j in range(0, len(final)):
		if final[j]==initial[i]:
			c=c+1
	if c!=0:
		newList.append(initial[i])

for i in range(0, len(newList)):
	with open('newList.txt','a') as helaData:
			helaWrite=csv.writer(helaData)
			helaWrite.writerow(newList[i])