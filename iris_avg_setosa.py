# Fisher's Iris Dataset Project - Iris Average Setosa
# Author Babu Baskaran
# Date 25.4.19 
# Plotting graph for Iris flowers
import matplotlib.pyplot as plt
import csv

a = []
b = []
c = []
d = []
count = 0

# slen = Seapal Length, swid = Seapal Width, plen = Petal Length, pwid = Petal Width
# slenav = Seapal Length Average, swidav = Seapal Width Average, plenav = Petal Length Average, pwidav = Petal Width Average
slen = 0
swid = 0
plen = 0
pwid = 0
slenav = 0
swidav = 0
plenav = 0
pwidav = 0


def avg(X,Y):
    avg = 0
    avg = X/Y

    return round(avg,2)

with open('irisdata.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       
        if row[4] == "Iris-setosa":
            a.append(float(row[0]))
            b.append(float(row[1]))
            c.append(float(row[0]))
            d.append(float(row[1]))

            count += 1
            
            slen += float(row[0])
            swid += float(row[0])
            plen += float(row[0])
            pwid += float(row[0])

slenav = avg(slen,count)
swidav = avg(swid,count)
plenav = avg(plen,count)
pwidav = avg(pwid,count)


plt.scatter(slenav,swidav, marker="^", label='Iris-setosa', color=['red'])
plt.scatter(plenav,pwidav, marker="<", label='Iris-setosa', color=['green'])


plt.xlabel("Average Length")
plt.ylabel("Average Width")
plt.title('Fishers Iris Setosa')
plt.legend()
plt.show()
