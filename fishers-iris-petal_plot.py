# Fisher's Iris Dataset Project
# Author Babu Baskaran
# Date 25.4.19 
# Plotting graph for Iris flowers petals
import matplotlib.pyplot as plt
import csv
import numpy as np


a = []
b = []
c = []
d = []
e = []
f = []

with open('irisdata.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
       
        if row[4] == "Iris-setosa":
            a.append(float(row[2]))
            b.append(float(row[3]))
        if row[4] == "Iris-versicolor":
            c.append(float(row[2]))
            d.append(float(row[3]))
        if row[4] == "Iris-virginica":
            e.append(float(row[2]))
            f.append(float(row[3]))
    

plt.scatter(a,b, marker="*",color='orange', label = 'Iris-setosa')
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title('Fishers Iris Data')
plt.legend()

# Fishers Iris versicolor
plt.scatter(c,d, marker=">",color='brown',label = 'Iris-versicolor')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()

# Fishers Iris-virginica
plt.scatter(e,f, marker="s",color='black',label = 'Iris-virginica')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()


plt.show()
