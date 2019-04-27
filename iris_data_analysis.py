# Fisher's Iris Dataset Project - Data analysis
# Author Babu Baskaran
# Date 27.4.19 
# import numpy and pandas
import numpy as np 
import pandas as pd 
#import csv

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt


dafile = "irisdata.csv"

# defining headers to the file
colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

datafile = pd.read_csv(dafile, names = colms)

datafile.info()

print(datafile.groupby('Species').size())

print(datafile.describe())

datafile.plot(kind='box', subplots = True, layout = (1,4), sharex = False, sharey = False, title='Summary Box Plot')

fig, ax = plt.subplots()

datafile.boxplot(column=['Sepal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
datafile.boxplot(column=['Petal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
datafile.boxplot(column=['Sepal_Width'], by='Species', ax=ax)

fig, ax = plt.subplots()
datafile.boxplot(column=['Petal_Width'], by='Species', ax=ax)

datafile.hist(bins=15)

scatter_matrix(datafile)

plt.show()
