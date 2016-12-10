# Python_Final_Project
Python Final Project

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


