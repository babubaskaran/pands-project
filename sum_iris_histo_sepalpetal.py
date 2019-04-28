# Fisher's Iris Dataset Project - Iris Average Setosa
# Author Babu Baskaran
# Date 27.4.19 
# Plotting graph for Iris flowers
# import matplotlib for graph
import matplotlib.pyplot as plt
import csv

# assigning x & y arrays for Seapl length, Petal length & Sepal width, Petal Width
slenx = []
pleny = []
swidx = []
pwidy = []

# nummber of rows for each flowers 
count = count2 = count3 = 0

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

# assigning array for overall average for length & width
olen = []
owid = []

# function for calculating the average of the length & width overall
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
            count2 += 1
            slen2 += float(row[0])
            swid2 += float(row[1])
            plen2 += float(row[2])
            pwid2 += float(row[3])
        if row[4] == "Iris-virginica":
            count3 += 1
            slen3 += float(row[0])
            swid3 += float(row[1])
            plen3 += float(row[2])
            pwid3 += float(row[3])

# finding average and assigning seapl and petal data - Iris Setosa
avslen1 = aveg(slen1,count)
avswid1 = aveg(swid1, count)
avplen1 = aveg(plen1,count)
avpwid1 = aveg(pwid1,count)

# sepal and petal added into overall length and width array - Iris Setosa
olen.append(avslen1)
olen.append(avplen1)
owid.append(avswid1)
owid.append(avpwid1)

# sapal and petal overall average added into overall sepal & petal into length & width array - Iris Setosa
slenx.append(avslen1)
swidx.append(avswid1)
pleny.append(avplen1)
pwidy.append(avpwid1)

# finding average and assigning seapl and petal data - Iris Versicolor
avslen2 = aveg(slen2,count2)
avswid2 = aveg(swid2, count2)
avplen2 = aveg(plen2,count2)
avpwid2 = aveg(pwid2,count2)

# sepal and petal added into overall length and width array - Iris Versicolor
olen.append(avslen2)
olen.append(avplen2)
owid.append(avswid2)
owid.append(avpwid2)

# sapal and petal overall average added into overall sepal & petal into length & width array  - Versicolor
slenx.append(avslen2)
swidx.append(avswid2)
pleny.append(avplen2)
pwidy.append(avpwid2)

# finding average and assigning seapl and petal data - Iris Virginica
avslen3 = aveg(slen3,count3)
avswid3 = aveg(swid3, count3)
avplen3 = aveg(plen3,count3)
avpwid3 = aveg(pwid3,count3)

# sepal and petal added into overall length and width array - Iris Virginica
olen.append(avslen3)
olen.append(avplen3)
owid.append(avswid3)
owid.append(avpwid3)

# sapal and petal overall average added into overall sepal & petal into length & width array  - Virginica
slenx.append(avslen3)
swidx.append(avswid3)
pleny.append(avplen3)
pwidy.append(avpwid3)


# Generating Histogram using hist for summary of average of Setosa, Versicolor & Virginica
plt.hist([olen,owid], bins=6, rwidth=0.70, label=['Sepal & Petal Width','Sepal & Petal Length'], color=['blue','red'])


plt.xlabel("Average Width and Length")
plt.ylabel("count")
plt.title('Fishers Iris Summary Average')
plt.legend()
plt.show()

            
