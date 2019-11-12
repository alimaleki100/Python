# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:49:27 2018

@author: a.maleki
"""

import pandas as pd
import numpy as np

SpotCrudePrices_2013_Data={
'UKB' : {'2013-Q1':112.9, '2013-Q2':103.0, '2013-Q3':110.1, '2013-Q4':109.4},
'Dubai':{'2013-Q1':108.1, '2013-Q2':100.8, '2013-Q3':106.1,'2013-Q4':106.7},
'WTI':{'2013-Q1':94.4, '2013-Q2':94.2, '2013-Q3':105.8,'2013-Q4':97.4}}

df=pd.DataFrame.from_dict(SpotCrudePrices_2013_Data)
print(df)


#select 1 column
dubaiPrices=df['Dubai']
print(dubaiPrices)
print(df.get('UKB'))
print(df.UKB)

#select 2 columns
print(df[['WTI','UKB']])

#Slicing
print(df[:2])
print(df[::2])




NYC_SnowAvgsData={'Months' :
['January','February','March',
'April', 'November', 'December'],
'Avg SnowDays' : [4.0,2.7,1.7,0.2,0.2,2.3],
'Avg Precip. (cm)' : [17.8,22.4,9.1,1.5,0.8,12.2],
'Avg Low Temp. (F)' : [27,29,35,45,42,32] }
#print(NYC_SnowAvgsData)
NYCdf=pd.DataFrame(NYC_SnowAvgsData,
index=NYC_SnowAvgsData['Months'],
columns=['Avg SnowDays','Avg Precip. (cm)',
'Avg Low Temp. (F)'])
print(NYCdf)


#using .loc to FIND ROWS

#Using a single label:

print(NYCdf.loc['January'])

#Using a list of labels:
print(NYCdf.loc[['January','April']])

#Using a label range:
print(NYCdf.loc['January':'April'])


#Select Column by loc
print(NYCdf.loc[:,'Avg SnowDays'])
print(NYCdf['Avg SnowDays'])


#select a cell bu loc
print(NYCdf.loc['March','Avg SnowDays'])

print(NYCdf.loc['March']['Avg SnowDays'])


#select row by BOOLEAN ARRAY
print(NYCdf.loc[NYCdf['Avg SnowDays']<1])


#####SELECT row MULTIPLE CONDITION
print(NYCdf.loc[(NYCdf['Avg SnowDays']<1) & (NYCdf['Avg Low Temp. (F)']==45)])


#IMPORTANT


print(df.loc[:,df.loc['2013-Q1']>100])




#Integer Oriented indexing
import scipy.constants as phys
import math

sci_values=pd.DataFrame([[math.pi, math.sin(math.pi),
math.cos(math.pi)],
[math.e,math.log(math.e),
phys.golden],
[phys.c,phys.g,phys.e],
[phys.m_e,phys.m_p,phys.m_n]],
index=list(range(0,20,5)))

print(sci_values)


print(sci_values.iloc[:2])
print('HELLLLLOOOOOO')
print(sci_values.iloc[2,2])






