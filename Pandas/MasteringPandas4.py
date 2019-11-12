# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:17:23 2018

@author: a.maleki
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
data=pd.read_excel("C:/Users/a.maleki/Desktop/PandasData.xlsx")
#print(data)
df=pd.DataFrame(data)
#print(df)
df=df.set_index('ID')

dict={"B":1,"M":2,"P":3}
df['Education']=df['Education'].apply(lambda x:dict.values())

print(df)
df.plot.scatter('Experience','Salary',marker="X")
dfpt=df.pivot_table(values='Salary',index='Position',columns='Nationality',aggfunc=np.mean)
print(dfpt)

df.plot.bar(x='Name',y=['Height','Weight'])

