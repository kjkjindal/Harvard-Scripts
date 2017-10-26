import csv

f1=file('finalTent.csv')
f2=file('poolmap.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)

final=list(r1)
pool=list(r2)
uniFinal=[]
uniPool=[]

for i in range(0, len(final)):
	c=0
	for j in range(0, len(pool)):
		if final[i][2]==pool[j][2]:
			c=c+1

	if c!=0:
		final[i]=0
		

for i in range(0, len(final)):
	if final[i]!=0:
		print (final[i])