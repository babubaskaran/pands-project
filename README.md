# Fisher's Iris Data Set Project 2019


This repository contains my  Project 2019 on Fisher's Iis Data Set.  The project entails doing research on the Iris Data Set and writing detailed documentation.  Background information about the data set and writing a summary of the same.  Summarise the dataset by writing Python Scripts.  Supported with tables and graphics to give overview of the Project.

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".

![ronald-fisher](https://user-images.githubusercontent.com/48861486/56838903-dc6c6900-6877-11e9-80eb-25758e5e3431.JPG)

## Description of Iris Data Set

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. 


![Kosaciec_szczecinkowaty_Iris_setosa](https://user-images.githubusercontent.com/48861486/56839483-9cf34c00-687a-11e9-9040-73e8284c8366.jpg)
![800px-Iris_virginica](https://user-images.githubusercontent.com/48861486/56839491-a086d300-687a-11e9-8b49-3f93aea338a1.jpg)
![800px-Iris_versicolor_3](https://user-images.githubusercontent.com/48861486/56839493-a2509680-687a-11e9-9f68-76efa0bcf811.jpg)

## Process Details

1. Research : Fisher's Iris Data and understanding how to data analysis
2. Load Iris Data in Python
3. Analysing the data and Visual Rrepresentation of Data

## Research and Developing:

* Data Analysis : Data analysis is a process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making. Data analysis has multiple facets and approaches, encompassing diverse techniques under a variety of names, and is used in different business, science, and social science domains. In today's business world, data analysis plays a role in making decisions more scientific and helping businesses operate more effectively.

The Project on Fisher's Iris Data Analysis using Python to identify varies types of patterns / variation or uncommon features the Iris Data set produce.



[See here for the instructions]https://github.com/babubaskaran/pands-project

## How to download this repository

1. Go to Github.
2. Click the download button.

## How to run the code

1. Make sure you have Python installed.
2. Make sure you have installed matplotlib
3. Make sure you have installed pandas


## Python Program for various data analysis

* fishers_iris_sepal_plot.py - This script will open irisdata.csv file using the csv library and get values of Sepal length and width of all 3 Iris flowers and generate a scatter graph which will show differnce between each flower.

![fishers_iris_sepal_plotpy](https://user-images.githubusercontent.com/48861486/56870048-069d6280-6a01-11e9-9617-352a367c911b.png)

* fishers_iris_petal_plot.py - This script will open irisdata.csv file using the csv library and get values of Petal length and width of all 3 Iris flowers and generate a scatter graph which will show differnce between each flower.

![fisher_iris_petal_plotpy](https://user-images.githubusercontent.com/48861486/56870141-aa3b4280-6a02-11e9-90b9-8bb86a7c3e14.png)

* iris_avg_setosa.py - This script will calculate the average of sepal and petal data of Iris Setosa flower and plotting the scatter graph.

![iris_avg_setosapy](https://user-images.githubusercontent.com/48861486/56870254-bfb16c00-6a04-11e9-8135-93e11219b2cd.png)

* iris_avg_versicolor.py - This script will calculate the average of sepal and petal data of Iris Versicolor flower and plotting the scatter graph.

![iris_avg_versicolor](https://user-images.githubusercontent.com/48861486/56870277-13bc5080-6a05-11e9-901c-18700d6f0df5.png)

* iris_avg_virginica.py - This script will calculate the average of sepal and petal data of Iris Virginica flower and plotting the scatter graph.

![iris_avg_virginicapy](https://user-images.githubusercontent.com/48861486/56870288-2f275b80-6a05-11e9-8cdf-d072e9238edb.png)


* sum_iris_sepalpetal.py - This script will calculate the average of sepal and petal data of all 3 Iris Setosa, Versicolor and Virginica flower and plotting the scatter graph.

![sum_iris_sepalpetalpy](https://user-images.githubusercontent.com/48861486/56870369-4a469b00-6a06-11e9-9a70-821b912f082c.png)

* Histogram Graphs to generate sets of data of each Flower and summary of everything.

* sum_iris_histo_sepalpetal.py - This script will calculate the average of Sepal and Petal data of all 3 Iris Setosa, Versicolor and Virginica flower and generate plot summary Histogram.

![sum_iris_histo_sepalpetalpy](https://user-images.githubusercontent.com/48861486/56870410-e2dd1b00-6a06-11e9-960f-dc611ede6081.png)

* Fisher's Iris Data Analysis using pandas and numpy library.

* Results and output of scripts explained below

* Each columns names generated on first part of the script

df.info()

![datafileinformation](https://user-images.githubusercontent.com/48861486/56870483-d6a58d80-6a07-11e9-8819-3cf46b97fee4.JPG)


* Number of rows of each type/species of flowers

print(df.groupby('Species').size())

![datafilesize](https://user-images.githubusercontent.com/48861486/56870501-3dc34200-6a08-11e9-9088-40281e1fa908.JPG)

* Display the count, mean, standard divation, minimum and maximum (length & width) of sepal and petal

print(df.describe())

![datafile](https://user-images.githubusercontent.com/48861486/56870536-c17d2e80-6a08-11e9-9f4d-7198322be18e.JPG)

* Box chart for mean, min and max and the outliers of each flower

![summaryboxplot](https://user-images.githubusercontent.com/48861486/56870552-26388900-6a09-11e9-887c-e9f7b48e821c.png)

* Box chart for each type Seapal Length, Petal Length, Sepal Width and Petal Width

![boxplotsepallength](https://user-images.githubusercontent.com/48861486/56870586-91825b00-6a09-11e9-9306-f3b477df34a4.png)

![boxplotpetallength](https://user-images.githubusercontent.com/48861486/56870590-9ba45980-6a09-11e9-8245-8b6398af436e.png)

![boxplotsepalwidth](https://user-images.githubusercontent.com/48861486/56870596-a363fe00-6a09-11e9-8cac-744092630ec2.png)

![boxplotpetalwidth](https://user-images.githubusercontent.com/48861486/56870600-a9f27580-6a09-11e9-99e5-7928102fd27b.png)

* Histogram with 15 containers to show the distribution of the flowers dimentions

![sum_iris_histo_sepalpetalpy](https://user-images.githubusercontent.com/48861486/56871037-26885280-6a10-11e9-90d6-2193c1c959c5.png)

* Summary Scatter Matrix

![scattermatrixchart](https://user-images.githubusercontent.com/48861486/56870629-0c4b7600-6a0a-11e9-80c4-93bf9b3beab4.png)

* fishers_iris_analysis_menu.py - This script will run as a menu where user can select what they wanted to see.

![menu](https://user-images.githubusercontent.com/48861486/56870669-aca19a80-6a0a-11e9-981e-bfeeb2e36d0f.JPG)

* Conclusion:

From Fisher’s Iris Data Analysis, I found it important to be able to reference graphs of the data with the statistical analysis run from the application. The most useful variables were petal length and petal width.  The sepal length and sepal width weren’t useful due to they overlapped each other and proved difficult to differentiate between the different species.
The Mean of the Sepal Length is 5.84 for all 3 flowers, Sepal width is 3.05, Petal Length is 3.75 and Petal width is 1.19.

The Min of the Sepal Length is 4.3 for all 3 flowers, Sepal width is 2.0, Petal Length is 1.0 and Petal width is 0.1.

The Max of the Sepal Length is 7.9 for all 3 flowers, Sepal width is 4.4, Petal Length is 6.9 and Petal width is 2.5.

Virginica is the largest iris while Setosa is the smallest








## References

* The Dataset https://archive.ics.uci.edu/ml/datasets/iris
 
* https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

* https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/

* https://help.github.com/en/articles/basic-writing-and-formatting-syntax

* https://www.youtube.com/watch?v=WbTOutpwPHs

* https://www.youtube.com/watch?v=snkkKrek7TU

* https://matplotlib.org/api/markers_api.html

* https://stackoverflow.com/questions/18498690/boxplot-with-pandas-groupby


