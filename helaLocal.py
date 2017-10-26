import csv


f1=file('filteredListH.csv')
f2=('filteredListM.csv')
f3=file('filteredListL.csv')
f4=file('filteredListND.csv')
f5=file('localData.csv')

r1=csv.reader(f1)
r2=csv.reader(f2)
r3=csv.reader(f3)
r4=csv.reader(f4)
r5=csv.reader(f5)

high=list(r1)
medium=list(r2)
low=list(r3)
nd=list(r4)
local=list(r5)

for i in range(1,len(local)):
	for j in range(1,len(high)):
		if local[i][0]==high[j][0]:
			high[j][6]="Cytoplasm"

		elif local[i][1]==high[j][0]:
			high[j][6]="Mitochondria"

		elif local[i][2]==high[j][0]:
			high[j][6]="Nucleus"

		elif local[i][3]==high[j][0]:
			high[j][6]="Cytoskeleton (Actin)"

		elif local[i][4]==high[j][0]:
			high[j][6]="Cytoskeleton (All)"

		elif local[i][5]==high[j][0]:
			high[j][6]="Focal Adhesion"

		elif local[i][6]==high[j][0]:
			high[j][6]="Endoplasmic Reticulum"

		elif local[i][7]==high[j][0]:
			high[j][6]="Golgi"

		elif local[i][8]==high[j][0]:
			high[j][6]="Nuclear Membrane"

		elif local[i][9]==high[j][0]:
			high[j][6]="Nucleoli"

		elif local[i][10]==high[j][0]:
			high[j][6]="Vescicles (All)"

		elif local[i][11]==high[j][0]:
			high[j][6]="Cell Junction"

		else:
			high[j][6]="None"


for i in range(1,len(local)):
	for j in range(1,len(medium)):
		if local[i][0]==medium[j][0]:
			medium[j][6]="Cytoplasm"

		elif local[i][1]==medium[j][0]:
			medium[j][6]="Mitochondria"

		elif local[i][2]==medium[j][0]:
			medium[j][6]="Nucleus"

		elif local[i][3]==medium[j][0]:
			medium[j][6]="Cytoskeleton (Actin)"

		elif local[i][4]==medium[j][0]:
			medium[j][6]="Cytoskeleton (All)"

		elif local[i][5]==medium[j][0]:
			medium[j][6]="Focal Adhesion"

		elif local[i][6]==medium[j][0]:
			medium[j][6]="Endoplasmic Reticulum"

		elif local[i][7]==medium[j][0]:
			medium[j][6]="Golgi"

		elif local[i][8]==medium[j][0]:
			medium[j][6]="Nuclear Membrane"

		elif local[i][9]==medium[j][0]:
			medium[j][6]="Nucleoli"

		elif local[i][10]==medium[j][0]:
			medium[j][6]="Vescicles (All)"

		elif local[i][11]==medium[j][0]:
			medium[j][6]="Cell Junction"

		else:
			medium[j][0]="None"



		for j in range(1,len(low)):
			if local[i][0]==low[j][0]:
				low[j][6]="Cytoplasm"

			elif local[i][1]==low[j][0]:
				low[j][6]="Mitochondria"

			elif local[i][2]==low[j][0]:
				low[j][6]="Nucleus"

			elif local[i][3]==low[j][0]:
				low[j][6]="Cytoskeleton (Actin)"

			elif local[i][4]==low[j][0]:
				low[j][6]="Cytoskeleton (All)"

			elif local[i][5]==low[j][0]:
				low[j][6]="Focal Adhesion"

			elif local[i][6]==low[j][0]:
				low[j][6]="Endoplasmic Reticulum"

			elif local[i][7]==low[j][0]:
				low[j][6]="Golgi"

			elif local[i][8]==low[j][0]:
				low[j][6]="Nuclear Membrane"

			elif local[i][9]==low[j][0]:
				low[j][6]="Nucleoli"

			elif local[i][10]==low[j][0]:
				low[j][6]="Vescicles (All)"

			elif local[i][11]==low[j][0]:
				low[j][6]="Cell Junction"

			else:
				low[j][6]="None"




		for j in range(1,len(nd)):
			if local[i][0]==nd[j][0]:
				nd[j][6]="Cytoplasm"

			elif local[i][1]==nd[j][0]:
				nd[j][6]="Mitochondria"

			elif local[i][2]==nd[j][0]:
				nd[j][6]="Nucleus"

			elif local[i][3]==nd[j][0]:
				nd[j][6]="Cytoskeleton (Actin)"

			elif local[i][4]==nd[j][0]:
				nd[j][6]="Cytoskeleton (All)"

			elif local[i][5]==nd[j][0]:
				nd[j][6]="Focal Adhesion"

			elif local[i][6]==nd[j][0]:
				nd[j][6]="Endoplasmic Reticulum"

			elif local[i][7]==nd[j][0]:
				nd[j][6]="Golgi"

			elif local[i][8]==nd[j][0]:
				nd[j][6]="Nuclear Membrane"

			elif local[i][9]==nd[j][0]:
				nd[j][6]="Nucleoli"

			elif local[i][10]==nd[j][0]:
				nd[j][6]="Vescicles (All)"

			elif local[i][11]==nd[j][0]:
				nd[j][6]="Cell Junction"

			else:
				nd[j][6]="None"



for i in range(0,len(high)):
	with open('filteredListHlocal.csv','a') as filterList:
				filterWrite=csv.writer(filterList)
				filterWrite.writerow(high[i])


for i in range(0,len(medium)):
	with open('filteredListLlocal.csv','a') as filterList:
				filterWrite=csv.writer(filterList)
				filterWrite.writerow(medium[i])


for i in range(0,len(low)):
	with open('filteredListLlocal.csv','a') as filterList:
				filterWrite=csv.writer(filterList)
				filterWrite.writerow(low[i])


for i in range(0,len(nd)):
	with open('filteredListNDlocal.csv','a') as filterList:
				filterWrite=csv.writer(filterList)
				filterWrite.writerow(nd[i])


