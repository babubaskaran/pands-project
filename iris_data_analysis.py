# Fisher's Iris Dataset Project - Data analysis
# Author Babu Baskaran
# Date 27.4.19 
# import numpy, pandas and matplotlib
import numpy as np 
import pandas as pd 
import csv

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt

# assigning irisdata.csv to datafile
dafile = "irisdata.csv"


# defining headers to the file

colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

# reading the delimited text file 
df = pd.read_csv(dafile,names=colms)

# Details of each column displayed
df.info()

# Number of data of each flowers displayed

print(df.groupby('Species').size())

# Detailed discription of minimum, maximum(length & width), mean, count & std diviation 
print(df.describe())

# plot box of mean, min and max of each flower
df.plot(kind='box', subplots = True, layout = (1,4), sharey = False, sharex = False, title='summary box plot' )

fig, ax = plt.subplots()

df.boxplot(column=['Sepal_Length'], by='Species', ax=ax)

# is a function that returns a tuple containing a figure and axes object

fig, ax = plt.subplots()
df.boxplot(column=['Petal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
df.boxplot(column=['Sepal_Width'], by='Species', ax=ax)

fig, ax = plt.subplots()
df.boxplot(column=['Petal_Width'], by='Species', ax=ax)

df.hist(bins=15)

scatter_matrix(df)

plt.show()
