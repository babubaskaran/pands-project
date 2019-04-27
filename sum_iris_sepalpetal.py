# Fisher's Iris Dataset Project - Iris Average Setosa
# Author Babu Baskaran
# Date 26.4.19 
# Plotting graph for Iris flowers
import matplotlib.pyplot as plt
import csv

slenx = []
pleny = []
swidx = []
pwidy = []

count = 0

# sepal and petal data - setosa(1)
slen1 = swid1 = plen1 = pwid1 = 0

# sepal and petal data - versicolor(2)
slen2 = swid2 = plen2 = pwid2 = 0

# sepal and petal data - Virginica(3)
slen3 = swid3 = plen3 = pwid3 = 0

# sepal and petal data average - setosa(1)
avslen1 = avswid1 = avplen1 = avpwid1 = 0

# sepal and petal data average - versicolor(2)
avslen2 = avswid2 = avplen2 = avpwid2 = 0

# sepal and petal data average - Virginica(3)
avslen3 = avswid3 = avplen3 = avpwid3 = 0

olen = []
owid = []

def aveg(x,y):

    aveg = 0
    aveg = x/y 

    return round(aveg,2)

with open('irisdata.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       
        if row[4] == "Iris-setosa":
            count += 1
            slen1 += float(row[0])
            swid1 += float(row[1])
            plen1 += float(row[2])
            pwid1 += float(row[3])
        if row[4] == "Iris-versicolor":
            count += 1
            slen2 += float(row[0])
            swid2 += float(row[1])
            plen2 += float(row[2])
            pwid2 += float(row[3])
        if row[4] == "Iris-virginica":
            count += 1
            slen3 += float(row[0])
            swid3 += float(row[1])
            plen3 += float(row[2])
            pwid3 += float(row[3])

# finding average and assigning seapl and petal data - Iris Setosa
avslen1 = aveg(slen1,count)
avswid1 = aveg(swid1, count)
avplen1 = aveg(plen1,count)
avpwid1 = aveg(pwid1,count)

olen.append(avslen1)
olen.append(avplen1)
owid.append(avswid1)
owid.append(avpwid1)

slenx.append(avslen1)
swidx.append(avswid1)
pleny.append(avplen1)
pwidy.append(avpwid1)

# finding average and assigning seapl and petal data - Iris Versicolor
avslen2 = aveg(slen2,count)
avswid2 = aveg(swid2, count)
avplen2 = aveg(plen2,count)
avpwid2 = aveg(pwid2,count)

olen.append(avslen2)
olen.append(avplen2)
owid.append(avswid2)
owid.append(avpwid2)

slenx.append(avslen2)
swidx.append(avswid2)
pleny.append(avplen2)
pwidy.append(avpwid2)

# finding average and assigning seapl and petal data - Iris Virginica
avslen3 = aveg(slen3,count)
avswid3 = aveg(swid3, count)
avplen3 = aveg(plen3,count)
avpwid3 = aveg(pwid3,count)

olen.append(avslen3)
olen.append(avplen3)
owid.append(avswid3)
owid.append(avpwid3)

slenx.append(avslen3)
swidx.append(avswid3)
pleny.append(avplen3)
pwidy.append(avpwid3)


plt.scatter(olen,owid, marker="s", label='overall average', color=['blue'])


plt.xlabel("Length")
plt.ylabel("Width")
plt.title('Fishers Iris Summary Average')
plt.legend()
plt.show()

            
