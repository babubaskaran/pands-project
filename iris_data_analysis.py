# Fisher's Iris Dataset Project - Data analysis
# Author Babu Baskaran
# Date 27.4.19 
# import numpy and pandas
import numpy as np 
import pandas as pd 
import csv

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt


dafile = "irisdata.csv"


# defining headers to the file

# colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']


df = pd.read_csv(dafile,names=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species'])


df.info()

print(df.groupby('Species').size())

print(df.describe())

df.plot(kind='box', subplots = True, layout = (1,4), sharey = False, sharex = False, title='summary box plot' )

fig, ax = plt.subplots()

df.boxplot(column=['Sepal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
df.boxplot(column=['Petal_Length'], by='Species', ax=ax)

fig, ax = plt.subplots()
df.boxplot(column=['Sepal_Width'], by='Species', ax=ax)

fig, ax = plt.subplots()
df.boxplot(column=['Petal_Width'], by='Species', ax=ax)

df.hist(bins=15)

plt.show()

scatter_matrix(df)

plt.show()
