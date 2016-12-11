
# coding: utf-8

# In[4]:

import matplotlib.pyplot as plt
import glob
import random
import numpy as np
import pandas as pd
import seaborn as sns
files='C:/Users/Shailesh Hegde/Desktop/PythonFinal/Accident_analysis.csv'
df1 =pd.read_csv(files)



df1["DATE"] = pd.to_datetime(df1["DATE"])
df1["DATE"].dt.year
print(df1.loc[(df1['VEHICLE TYPE CODE 1'] == 'PASSENGER VEHICLE') & (df1['NUMBER OF MOTORIST KILLED'] == 1) & (df1['DATE'] == 2016) & (df1['CONTRIBUTING FACTOR VEHICLE 1'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 2'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 3'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 4'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 5'] == 'Alcohol Involvement')])
df_new=df1.loc[(df1['VEHICLE TYPE CODE 1'] == 'PASSENGER VEHICLE') & (df1['NUMBER OF MOTORIST KILLED'] == 1) & (df1['DATE'] == 2016) & (df1['CONTRIBUTING FACTOR VEHICLE 1'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 2'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 3'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 4'] == 'Alcohol Involvement') & (df1['CONTRIBUTING FACTOR VEHICLE 5'] == 'Alcohol Involvement')]
print(df_new)


# In[ ]:




# In[ ]:




# In[ ]:



