import csv

totaldata = []

with open('mainecounties.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        totaldata.append(row)

newdata = []

for d in totaldata[-17:-1]:
	newdata.append([d[1],d[4],d[5]])

newdata.append([totaldata[-1][1],totaldata[-1][4],totaldata[-1][5]])

if newdata[0][0] != "Androscoggin":
        print("ERROR, data is not in right format")
for d in newdata:
	if d[0] == 'Unknown':
		newdata.remove(d)
print(newdata)
f = open("updatedcoronadata.js","w")
f.write("let updated_data = ")

f.write("[")

for d in newdata:
	f.write(str(d))
	f.write(",")

f.write("]")
f.close()
