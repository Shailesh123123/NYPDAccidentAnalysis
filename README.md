# Python_Final_Project

# Project

On the basis of NYPD accident dataset which was obtained in the form of a .csv file from an unclean dataset from the link https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95 , 5 analysis were performed on the cleaned dataset eventually.

# Data Cleaning.

Data cleaning was performed on the type of analysis that was to be performed further, the basic rule of removing nulls and NAN's, especially from the columns having the most nulls was carried out initially and later data cleaning was done on the basis of analysis perfromed so as to not lose important data.

# Analysis

Analysis 1:


Plot a bar chart using matplotlib that represents each Borough(Counties) against the number of motorist injured for the multivariant conditions icluding that VEHICLE TYPE CODE 1 = PASSENGER VEHICLE and NUMBER OF MOTORIST KILLED = 1.

Steps:

Step-1:
Extract the cleaned dataset file which is in the .csv format by reading it into a dataframe.
Step-2:
Apply the conditions that include checking if VEHICLE TYPE CODE 1 = PASSENGER VEHICLE and NUMBER OF MOTORIST KILLED = 1
step-3:
Put this into a new dataframe
Step-4:
Now plot a bar graph using matplotlib by assigning the x-axis and y-axis with values corresponding to 'BOROUGH' and 'NUMBER OF MOTORIST INJURED' respectively.

# Output graph

[\Users\Shailesh Hegde\Desktop\Python\DataAnalysisPython\Python_final\Analysis.png](https://github.com/Shailesh123123/Python_Final_Project/edit/master/README.md)


Analysis 2:
Find out how the number of persons injured has stacked up every year from 2012 to 2016 by plotting a histogram

steps:
step-1:
Extract the cleaned dataset file which is in the .csv format by reading it into a dataframe.
Step-2:
Extract year substring from date string using pd.to_datetime(df1["DATE"]) and df1["DATE"].dt.year.
step-3:
using the group-by function, find the sum of number of motorists killed,injured,oersons killed and inkured and same for pedestrians and cyclists grouped by date.
Steps-4:
Transfer the result into a new dataframe.
step 5:
Plot a histogram using dataframe.hist() function keeping 2014 as the threshold to obtain the histogram.

# Output Graph

[\Users\Shailesh Hegde\Desktop\Python\DataAnalysisPython\Python_final\Analysis2.png](https://github.com/Shailesh123123/Python_Final_Project/edit/master/README.md)

Analysis 3:
Plot the number of motorists,persons and pedestrians injured for VEHICLE TYPE CODE 1 = PASSENGER VEHICLE using a line graph plot.
step-1:
Extract the cleaned dataset file which is in the .csv format by reading it into a dataframe.
Step-2:
Extract year substring from date string using pd.to_datetime(df1["DATE"]) and df1["DATE"].dt.year.
step-3:
Transfer the result into a new dataframe.
step-4:
using the group-by function, find the sum of number of motorists injured,injured,persons injured and pedestrians injured and same for pedestrians and cyclists grouped by VEHICLE TYPE CODE 1.
step-5:
Plot a line graph with VEHICLE TYPE CODE 1 on the x-axis and  sum of number of motorists injured,injured,persons injured and pedestrians injured and same for pedestrians and cyclists on the y-axis

# Output Graph

[\Users\Shailesh Hegde\Desktop\Python\DataAnalysisPython\Python_final\Analysis3.png](https://github.com/Shailesh123123/Python_Final_Project/edit/master/README.md)

Analysis-4:
Plot a pie chart that represents 'NUMBER OF MOTORIST INJURED', 'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PERSONS INJURED', 'NUMBER OF CYCLIST INJURED' for the Borough=Brooklyn.

step-1:
Extract the cleaned dataset file which is in the .csv format by reading it into a dataframe.
Step-2:
Extract year substring from date string using pd.to_datetime(df1["DATE"]) and df1["DATE"].dt.year.
step-3:
Transfer the result into a new dataframe.
step-4:
Use the group-by function to find the sum of all the aggregate capable attributes including the number of mororists killed,etc for the borough Brooklyn.
step-5:
Plot a pie chart that represents 'NUMBER OF MOTORIST INJURED', 'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PERSONS INJURED', 'NUMBER OF CYCLIST INJURED' for the Borough=Brooklyn.

# Output Graph

[\Users\Shailesh Hegde\Desktop\Python\DataAnalysisPython\Python_final\Analysis4.png](https://github.com/Shailesh123123/Python_Final_Project/edit/master/README.md)

Analysis-5:
For the Borough Brooklyn and the year 2016 find the most common occuring contributing factor-1 for accidents and plot the graph for their respective counts

step-1:
Extract the cleaned dataset file which is in the .csv format by reading it into a dataframe.
Step-2:
Extract year substring from date string using pd.to_datetime(df1["DATE"]) and df1["DATE"].dt.year.
step-3:
Transfer the result into a new dataframe.
step-4:
Use the group-by function to find the sum of all the aggregate capable attributes including the number of mororists killed,etc for the borough Brooklyn.
step-5:
Further filter the data on the basis of multivariant conditions inlcluding the ones that date = 2016 and borough = Brooklyn.
step-6:
Use group by function to get the aggregated cont of maximum count of each type from CONTRIBUTING FACTOR VEHICLE 1.
step-7:
plot a bar graph with the aggregated count on the y-axis and name of the contributing vehicle on the x-axis.

# Output Graph

[\Users\Shailesh Hegde\Desktop\Python\DataAnalysisPython\Python_final\Analysis5.png](https://github.com/Shailesh123123/Python_Final_Project/edit/master/README.md)
