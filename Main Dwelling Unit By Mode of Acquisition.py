# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:50:55 2020

@author: KIRIMI
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\KIRIMI\Documents\GitHub\Housing-Situation-2019-Census-Analysis\Data\volume_4-table-2.11a_-main-dwelling-unit-by-mode-of-acquisition-area-of-residence-county-and-sub.csv')
df.head(5)
df.info
df.columns
df.iloc[0:10,:5]
df.dtypes
columns=(['No', 'Owned', 'Purchased Number',
       'Purchased per cent', 'Mode of Acquisition ConstructedNumber',
       'Mode of Acquisition ConstructedNumber per cent', 'InheritedNumber',
       'Inherited per cent'])
df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
df.drop('No', axis=1, inplace=True)
Data = ['Rural', 'Urban', 'Mombasa', 'Kisumu', 'Nakuru', 'Nairobi city', 'Uasin Gishu']
df1=df[df['County/ Sub-County'].str.contains(r'^({})$'.format('|'.join(Data)), case=False)]
df1.columns
df1= df1.drop(['Purchased per cent',
       'Mode of Acquisition ConstructedNumber per cent',
       'Inherited per cent'], axis=1)
df1.head(6)
df1.set_index('County/ Sub-County', inplace=True)
df1 = df1.T
df1.reset_index(inplace=True)
df1.head(6)
df1['index']
df1.iloc[:1,1:3]
#Rural and Urban Comparison
plt.style.use('seaborn-talk')
fig, ax = plt.subplots(figsize=(6.3,6.3))
#plt.style.use('seaborn')
textprops={'color:#CFBDA3'}, 
ax.pie(df1.iloc[:1,1:3], colors=['#838996', '#b2d8d8'], labels=df1.iloc[:1,1:3].columns, autopct='%1.f%%', 
       radius=1.2, startangle=25, textprops=dict(color = '#000000', fontsize=14))
ax.set_title('Kenya\'s Rural and Urban Homeownership Rates, Census 2019', fontsize=14)
plt.tight_layout()

plt.show()

#Major Counties ('MOMBASA', 'UASIN GISHU', 'NAKURU', 'KISUMU', 'NAIROBI CITY') Mode of Aquisition of Dwelling
df2 = df1.drop(0, axis=0)
df2.set_index('index', inplace=True)
df2.columns
df2=df2.drop(['Rural', 'Urban'], axis=1)
df2=df2.T
df2=df2.reset_index()
df2['Total Homeownership']=df2.iloc[:, 1:].sum(axis=1)
population_to_percent = lambda x: x/df2['Total Homeownership']*100
columns_2 = (['Purchased Number',
       'Mode of Acquisition ConstructedNumber', 'InheritedNumber',
       'Total Homeownership'])
df2[columns_2]=df2[columns_2].apply(population_to_percent).round(0)

x = np.arange( len(df2['County/ Sub-County'].unique()))
fig, ax = plt.subplots(figsize=(9,5))
barwidth=0.25
rects1= ax.bar(x, df2['Purchased Number'], width=barwidth)
rects2=ax.bar(x + barwidth, df2['Mode of Acquisition ConstructedNumber'], width=barwidth)
rects3=ax.bar(x + barwidth*2, df2['InheritedNumber'], width=barwidth)
ax.set_xticklabels(df2['County/ Sub-County'].unique(), fontsize=14)
ax.set_xticks(x + barwidth)
ax.set_xlabel('County', fontsize=14)
ax.set_ylabel('% of County Population', fontsize=14)
ax.set_title('Counties (hosting major cities) Main Mode of Dwelling Aquisition, Census 2019', fontsize=14)
ax.legend(handles=[rects1,rects2, rects3 ], title='Mode of Acquisition', labels=['Purchased','Constructed', 
          'Inherited'], title_fontsize=12, fontsize=12)
def autolabel(rects):
    for rect in rects:
        yval = rect.get_height()
        ax.text(rect.get_x(), yval + 1.8, yval, fontsize=12)
        
ax.annotate('Source:KNBS, Census 2019\nCode:https://github.com/kriskirimi/', (0,0), (00,-45), fontsize=10, 
             xycoords='axes fraction', textcoords='offset points')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.style.use('seaborn-darkgrid')
plt.show()