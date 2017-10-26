import csv

f1=file('data.csv')
row=10;

data=csv.reader(f1)
col=[0]
col.append(1)

dataList=list(data)

for i in range(0,2):
	for j in range(0,9):
		print dataList[j][i]
	
for i in range(0,2):
	for j in range(0,9):
		
		print col[1]
		print dataList[j][i]



import random

random.randint(0,100)

f1=file('data.csv')
(array([ 2.,  1.,  1.,  0.,  2.,  0.,  1.,  0.,  0.,  2.]),
 array([  1. ,   1.9,   2.8,   3.7,   4.6,   5.5,   6.4,   7.3,   8.2,
          9.1,  10. ]),
 <a list of 10 Patch objects>)