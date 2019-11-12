# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:11:29 2018

@author: a.maleki
"""

import pandas as pd






data=pd.read_excel("C:/Users/a.maleki/Desktop/crf2.xlsx")
#print(data)
df=pd.DataFrame(data)

#print(df.groupby('Year'))

#calc sum of a column
print(df['UNIT SALES'].sum())


#delete row by condition
df2=df.ix[df['Month'] ==('JAN')]
print(df2)

#create a new excel file
writer=pd.ExcelWriter('C:/Users/a.maleki/Desktop/crf6.xlsx',engine='xlsxwriter')
df2.to_excel(writer, sheet_name='new')
writer.save()



#print(df.filter(like='BDF NIVEA',axis=0))

YYY= df[df['Holding'] == "YYYY"]
print(YYY)


