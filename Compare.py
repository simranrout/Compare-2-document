import csv
t1 = open('old.csv', 'r')
t2 = open('new.csv', 'r')
fileone = t1.readlines()
filetwo = t2.readlines()
t1.close()
t2.close()

outFile = open('update.csv', 'w')
x = 0
for i in fileone:
    if i != filetwo[x]:
        outFile.write(filetwo[x])
    x += 1
outFile.close()