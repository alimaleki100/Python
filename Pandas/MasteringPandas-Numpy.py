# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:14:48 2018

@author: a.maleki
"""

import numpy as np
import calendar as cal
import pandas as pd

#NUMPY 
ar1=np.array([0,4,6,1,6,2]) #1D Array
ar2=np.array([[1,4],[3,7],[8,11]]) #2D Array
print(ar1)
print()
print(ar2)

print(ar2.shape)
print(ar2.ndim)

ar3=np.arange(15,45,3)
ar3=ar3.reshape(2,5)
print(ar3)

# PANDAS SERIES
monthNames=[cal.month_abbr[1:13]]
months=pd.Series(np.arange(1,13),index=monthNames)
print(months)


currDict={'US':'Dollar', 'UK':'Pound', 'IR':'IRR',
          'MX':'PESO','JP':'YEN', 'CH':'YUAN', 
          'GR':'EURO'}

curr=pd.Series(currDict)
print(curr)

print(curr['CH'])
GradesDict={'Ali':20, 'Maryam':19, 'Reza':18,
          'Majid':2,'Homa':8, 'Bahram':9, 
          'Kobra':16}
Grades=pd.Series(GradesDict)
print(Grades)
print('Mean',np.mean(Grades))
print('Average',np.average(Grades))
print('SQRT',np.sqrt(Grades))

#PANDAS DATAFRAME

stockSummaries={
'AMZN': pd.Series([346.15,0.59,459,0.52,589.8,158.88],
index=['Closing price','EPS',
'Shares Outstanding(M)',
'Beta', 'P/E','Market Cap(B)']),
'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
index=['Closing price','EPS','Shares Outstanding(M)',
'Beta','P/E','Market Cap(B)']),
'FB': pd.Series([61.48,0.59,2450,104.93,150.92],
index=['Closing price','EPS','Shares Outstanding(M)',
'P/E', 'Market Cap(B)']),
'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
index=['Closing price','EPS','Shares Outstanding(M)',
'P/E','Beta', 'Market Cap(B)']),
'TWTR':pd.Series([65.25,-0.3,555.2,36.23],
index=['Closing price','EPS','Shares Outstanding(M)',
'Market Cap(B)']),
'AAPL':pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
index=['Closing price','EPS','Shares Outstanding(M)','P/E',
'Market Cap(B)','Beta'])}

stockDF=pd.DataFrame(stockSummaries,
index=['Closing price','EPS',
'Shares Outstanding(M)',
'P/E', 'Market Cap(B)','Beta']);stockDF
print(stockDF)

print(stockDF['AAPL'])



memberData = np.zeros((4,),
dtype=[('Name','a15'),
('Age','i4'),
('Weight','f4')])
memberData[:] = [('Sanjeev',37,162.4),
('Yingluck',45,137.8),
('Emeka',28,153.2),
('Amy',67,101.3)]

memberDF=pd.DataFrame(memberData)
print(memberDF)

memberDF=memberDF.set_index('Name')
print(memberDF)
print(memberDF['Age'])