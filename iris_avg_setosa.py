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