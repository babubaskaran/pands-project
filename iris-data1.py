# Python Project 1
# Author Babu Baskaran
# Date 24.4.19 
# Plotting graph for Iris flowers
import matplotlib.pyplot as plt
import csv

x = []
y = []
a = []
b = []
c = []
d = []


with open('iris_data.csv','r') as csvfile:
    plots = csv.reader(csvfile) #, delimiter=',')
    for row in plots:
        print(plots)
#        if row[4] == "Iris-setosa":
#            x.append(float(row[0]))
#            y.append(float(row[1]))
#        if row[4] == "Iris-versicolor":
#            a.append(float(row[0]))
#            b.append(float(row[1]))
#        if row[4] == "Iris-virginica":
#            c.append(float(row[0]))
#            d.append(float(row[1]))
    

#plt.scatter(x,y, marker="*", label='Iris-setosa', color=['red','yellow'])
#plt.ylabel('Sepal Length')
#plt.xlabel('Sepal Width')
#plt.title('Fishers Iris Data')
#plt.legend()

#plt.scatter(a,b, marker="<", label='Iris-versicolor', color=['blue','orange'])
#plt.xlabel('Sepal Length')
#plt.ylabel('Sepal Width')
# plt.title('Fishers Iris versicolor')
#plt.legend()

#plt.scatter(c,d, marker="s", label='Iris-virginica', color=['green','brown'])
#plt.xlabel('Sepal Length')
#plt.ylabel('Sepal Width')
# plt.title('Fishers Iris-virginica')
#plt.legend()


#plt.show()
