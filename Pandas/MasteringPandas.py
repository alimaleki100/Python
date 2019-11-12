# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:00:20 2018

@author: a.maleki
"""
import pandas as pd
import numpy as np
data=pd.read_excel("C:/Users/a.maleki/Desktop/PandasData.xlsx")
#print(data)
df=pd.DataFrame(data)
#print(df)
df=df.set_index('ID')
#print(df)


#column selection
#print(df['Name'])


#row selection
print(df[df['Position']=='Programmer'])

#del column
#del df['Height']
print(df)


#Mathematical Operations
#print(np.sqrt(df['Height']))

print(df.loc[9889])


