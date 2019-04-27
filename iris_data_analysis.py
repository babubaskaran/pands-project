# Fisher's Iris Dataset Project - Data analysis
# Author Babu Baskaran
# Date 27.4.19 
# import numpy and pandas
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

dafile = "irisdata.csv"

# defining headers to the file
columns = ['Sepal-Length','Sepal-Width','Petal-Length','Petal-Width','Species']

datafile = pd.read_csv(dafile,names=columns)

datafile.info()

print(datafile.groupby('Species').size())