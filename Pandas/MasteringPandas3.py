# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:52:27 2018

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


#CONCAT FUNCTION
#print(df)
a=df.loc[:,['Name','Position']]
print(a)

b=df.loc[:,['Nationality', 'Height']]
print(b)
print(pd.concat([a,b],axis=1))

#/////GROUPBY////
positionGrp=df.groupby('Position')
print(positionGrp.size())


nationPositionGrp=df.groupby(['Nationality','Position'])
print(nationPositionGrp.size())

nga=positionGrp.aggregate(np.sum)
print(nga)


ngadrop=nga.drop(['Salary'],axis=1)
print(ngadrop)
df.plot.scatter('Height','Weight')