# Fisher's Iris Dataset Project - Data analysis Menu
# Author Babu Baskaran
# Date 28.4.19 
# import numpy and pandas
import numpy as np 
import pandas as pd 

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt


df = "irisdata.csv"


# defining headers to the file

# colms = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']


df = pd.read_csv(df,names=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species'])

def menu():

    print('1. Information')
    print('2. Summary')
    print('3. Data')
    print('4. Box Chart - Summ')
    print('5. Box Chart - Detailed')
    print('6. Histogram')
    print('7. Scatter Matrix')
    print('8. Exit')

while True:
    menu()
    try:
        user_input = int(input("Enter a Number :"))
        if user_input == 1:
            print(df.info())
        elif user_input == 2:
            print(df.describe())
        elif user_input == 3:
            print(df)
        elif user_input == 4:
            df.plot(kind='box', subplots = True, layout = (1,4), sharey = False, sharex = False, title='summary box plot',figsize = (12,9) )

            plt.show()
        elif user_input == 5:
            fig, ax = plt.subplots()
            df.boxplot(column=['Sepal_Length'], by='Species', ax=ax)

            fig, ax = plt.subplots()
            df.boxplot(column=['Petal_Length'], by='Species', ax=ax)

            fig, ax = plt.subplots()
            df.boxplot(column=['Sepal_Width'], by='Species', ax=ax)

            fig, ax = plt.subplots()
            df.boxplot(column=['Petal_Width'], by='Species', ax=ax)
            plt.show()
        elif user_input == 6:
            df.hist(bins=15)
        elif user_input == 7:
            scatter_matrix(df)
            plt.show()
        elif user_input == 8:
            print('Thank you for looking at my project')
            break
        else:
            print('Incorrect option entered... Please enter the number between 1 to 8')
    except :
        print('Incorrect selection please enter number between 1 to 8')
