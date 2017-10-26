import csv

f1=file('HeLaSomamersAll.csv')
targets=csv.reader(f1)


probeList=list(targets)

for i in range(1,len(probeList)):
	if probeList[i][5]=="Not detected":
		with open('filteredListND.csv','a') as filterList:
			filterWrite=csv.writer(filterList)
			filterWrite.writerow(probeList[i])

	elif probeList[i][5]=="Low":
		with open('filteredListL.csv','a') as filterList:
			filterWrite=csv.writer(filterList)
			filterWrite.writerow(probeList[i])

	elif probeList[i][5]=="Medium":
		with open('filteredListM.csv','a') as filterList:
			filterWrite=csv.writer(filterList)
			filterWrite.writerow(probeList[i])


	elif probeList[i][5]=="High":
		with open('filteredListH.csv','a') as filterList:
			filterWrite=csv.writer(filterList)
			filterWrite.writerow(probeList[i])


	else:
		with open('filteredListMISC.csv','a') as filterList:
			filterWrite=csv.writer(filterList)
			filterWrite.writerow(probeList[i])

