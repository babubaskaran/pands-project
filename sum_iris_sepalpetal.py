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

            
