# Fisher's Iris Dataset Project - Iris Sepal Plot
# Author Babu Baskaran
# Date 24.4.19 
# Plotting graph for Iris flowers
import matplotlib.pyplot as plt
import csv

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
            a.append(float(row[0]))
            b.append(float(row[1]))
        if row[4] == "Iris-versicolor":
            c.append(float(row[0]))
            d.append(float(row[1]))
        if row[4] == "Iris-virginica":
            e.append(float(row[0]))
            f.append(float(row[1]))
    

plt.scatter(a,b, marker="*",label='Iris-setosa',color=['red'] )
plt.ylabel("Sepal Length")
plt.xlabel("Sepal Width")
plt.title('Fishers Iris Data')
plt.legend()

# Fishers Iris versicolor
plt.scatter(c,d, marker=">",color=['blue'],label = 'Iris-versicolor')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()

# Fishers Iris-virginica
plt.scatter(e,f, marker="s",color=['orange'],label = 'Iris-virginica')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()


plt.show()
