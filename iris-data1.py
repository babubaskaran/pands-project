# Python Project 1
# Author Babu Baskaran
# Date 24.4.19 
# Plotting graph for Iris flowers
import matplotlib.pyplot as plt
import csv
a = []
b = []

with open('iris_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
     if row[4] == "Iris-setosa":
        a.append(float(row[0]))
        b.append(float(row[1]))

plt.scatter(a,b, marker="*", label='Iris-setosa Details', color=['red','green'])
plt.ylabel('Sepal Length')
plt.xlabel('Sepal Width')
plt.title('Fishers Iris Data')
plt.legend()

plt.show()
