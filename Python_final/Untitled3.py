
# coding: utf-8

# In[1]:

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
#df_new = df1.groupby(["VEHICLE TYPE CODE 1"]).sum()
#print(df_new)
df1.plot.line(x='VEHICLE TYPE CODE 1', y=['NUMBER OF MOTORIST INJURED','NUMBER OF PEDESTRIANS INJURED','NUMBER OF PERSONS INJURED','NUMBER OF CYCLIST INJURED'])
print('here')
plt.show()



# In[8]:

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


# In[6]:

from matplotlib.pyplot import pie, axis, show
import matplotlib.pyplot as plt
import glob
import random
import numpy as np
import pandas as pd
import seaborn as sns

from __future__ import division
import numpy as np

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

# adding the PySpark modul to SparkContext
sc.addPyFile("https://raw.githubusercontent.com/seahboonsiew/pyspark-csv/master/pyspark_csv.py")
import pyspark_csv as pycsv

collisions = sc.textFile("swift://" + credentials['container'] + "." + credentials['name'] + "/NYPD_Motor_Vehicle_Collisions.csv")

def skip_header(idx, iterator):
    if (idx == 0):
        next(iterator)
    return iterator

collisions_header = collisions.first()


collisions_header_list = collisions_header.split(",")
collisions_body = collisions.mapPartitionsWithIndex(skip_header)

# filter not valid rows
collisions_body = collisions_body.filter(lambda line : len(line.split(","))>29)

# create Spark DataFrame using pyspark-csv
collisions_df = pycsv.csvToDataFrame(sqlContext, collisions_body, sep=",", columns=collisions_header_list)
collisions_df.cache()

collisions_pd = collisions_df[collisions_df['LATITUDE'] != 0][['LATITUDE', 'LONGITUDE', 'DATE', 'TIME',
                                                               'BOROUGH', 'ON STREET NAME', 'CROSS STREET NAME',
                                                               'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED',
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
df_new = df1.groupby([df1["DATE"].dt.year]).sum()


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
df_new = df1.groupby([df1["DATE"].dt.year]).sum()


# In[ ]:



