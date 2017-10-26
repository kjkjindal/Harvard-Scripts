import csv

f1=file('data.csv')
row=10;

data=csv.reader(f1)


dataList=list(data)
dataCol=[]
newList=[]


for i in range (0,2):

	for k in range(0,8):
		dataCol.append(int(dataList[k][i]))
	print dataCol



import random

random.randint(0,100)

	