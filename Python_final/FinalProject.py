
# coding: utf-8

# # Analysis 1: Plot a bar chart using matplotlib that represents each Borough(Counties) against the number of motorist injured for the multivariant conditions icluding that VEHICLE TYPE CODE 1 = PASSENGER VEHICLE and NUMBER OF MOTORIST KILLED = 1.

# In[1]:


import matplotlib.pyplot as plt
import glob
import random
import numpy as np
import pandas as pd
import seaborn as sns
files='C:/Users/Shailesh Hegde/Desktop/PythonFinal/Accident_analysis.csv'
df1 =pd.read_csv(files)
        
#print(df_new)
print(df1.loc[(df1['VEHICLE TYPE CODE 1'] == 'PASSENGER VEHICLE') & (df1['NUMBER OF MOTORIST KILLED'] == 1)])
df_new=df1.loc[(df1['VEHICLE TYPE CODE 1'] == 'PASSENGER VEHICLE') & (df1['NUMBER OF MOTORIST KILLED'] == 1)]
df_new.plot.bar(x='BOROUGH', y='NUMBER OF MOTORIST INJURED')
print('here')
plt.show()


# # Analysis 2 (Find out how the number of persons injured has stacked up every year from 2012 to 2016)

# In[9]:

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
df1.groupby([df1["DATE"].dt.year]).sum()
#df_new = df1.groupby([df1["DATE"].dt.year]).sum()
print(df1)
df1.reset_index(drop=True)
df1.plot.line(x='DATE', y=['NUMBER OF MOTORIST INJURED','NUMBER OF PEDESTRIANS INJURED'])

print('here')
plt.show()


# # Analysis 3: Plot the number of motorists,persons and pedestrians injured for VEHICLE TYPE CODE 1 = PASSENGER VEHICLE using a line graph plot.

# In[7]:

from matplotlib.pyplot import pie, axis, show
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
df1.groupby(["VEHICLE TYPE CODE 1"]).sum()
df1.loc[(df1['VEHICLE TYPE CODE 1'] == 'PASSENGER VEHICLE')]
print(df1)
#print(df1.groupby(["VEHICLE TYPE CODE 1"]).sum())
#df_new = df1.groupby(["VEHICLE TYPE CODE 1"]).sum()
#print(df_new)
df1.plot.line(x='VEHICLE TYPE CODE 1', y=['NUMBER OF MOTORIST INJURED','NUMBER OF PEDESTRIANS INJURED','NUMBER OF PERSONS INJURED','NUMBER OF CYCLIST INJURED'])
print('here')
plt.show()


# # Analysis 4: lot a pie chart that represents 'NUMBER OF MOTORIST INJURED', 'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PERSONS INJURED', 'NUMBER OF CYCLIST INJURED' for the Borough=Brooklyn.
# 

# In[6]:

from matplotlib.pyplot import pie, axis, show
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
df1.groupby(["BOROUGH"]).sum()
print(df1.groupby(["BOROUGH"]).sum())
df_new=df1.loc[(df1['BOROUGH'] == 'BROOKLYN')]
print(df_new)
#df_new = df1.groupby(["VEHICLE TYPE CODE 1"]).sum()
#print(df_new)
#df_new.plot.pie(x='BOROUGH', y=['NUMBER OF MOTORIST INJURED','NUMBER OF PEDESTRIANS INJURED','NUMBER OF PERSONS INJURED','NUMBER OF CYCLIST INJURED'])
df_new = pd.DataFrame(3 * np.random.rand(4, 1), index=['NUMBER OF MOTORIST INJURED', 'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PERSONS INJURED', 'NUMBER OF CYCLIST INJURED'], columns=['BOROUGH'])
df_new.plot.pie(subplots=True, figsize=(8, 4))

print('here')
plt.show()


# # Analysis-5, For the Borough Brooklyn and the year 2016 find the most common occuring contributing factor-1 for accidents and plot the graph for their respective counts

# In[5]:

import matplotlib.pyplot as plt
import glob
import random
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

files='C:/Users/Shailesh Hegde/Desktop/PythonFinal/Accident_analysis.csv'
df1 =pd.read_csv(files)
        
df1["DATE"] = pd.to_datetime(df1["DATE"])
df1["DATE"].dt.year
df1.groupby([df1["DATE"].dt.year]).sum()
#print(df1.groupby([df1["DATE"].dt.year]).sum())
#print(df1.loc[(df1['BOROUGH'] == 'BROOKLYN') & (df1["DATE"].dt.year == 2016)])
df_new=pd.DataFrame({'Count':df1.groupby(df1['VEHICLE TYPE CODE 1']).size()}).reset_index()
print(df_new)
#source = pd.DataFrame(df1)
#source.groupby([df1["CONTRIBUTING FACTOR VEHICLE 1"]]).agg(lambda x:x.value_counts().index['CONTRIBUTING FACTOR VEHICLE 1'])
#df1.plot.bar(x='BOROUGH', y='COUNT')

df_new.plot.bar(x='VEHICLE TYPE CODE 1', y='Count')
print('here')
plt.show()




# In[ ]:




# In[ ]:



