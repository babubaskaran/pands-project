import pandas as pd
import matplotlib.pyplot as plt


data = "irisdata.csv"
fig, ax = plt.subplots()
plt.suptitle('')
data.boxplot()
#data.boxplot(column='SepalLength', by='Name', ax=ax)
#data.boxplot(column=['SepalLength', 'SepalWidth'], by='Name', ax=ax)
plt.suptitle('') 



