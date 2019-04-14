# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:02:43 2019

@author: khushal
"""

import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from datetime import datetime
import numpy as np

img = io.BytesIO()
plt.style.use('ggplot')

#ax=plt.gca()
#plt.figure(dpi=250,figsize=(250,200))

pd.set_option('display.max_columns',1000)
path_of_input_file = "C:/Users/khushal/Documents/Python Scripts/StateUT-wise educational status of suicide victim during 2001-2012.xls"
input_data_df = pd.read_excel(path_of_input_file)
#input_data_df['Year'] = pd.to_datetime(input_data_df['Year'], format='%Y')
input_data_df['Year'].apply(pd.to_datetime)
input_data_df_MH = input_data_df[input_data_df['STATE/UT'] =='MAHARASHTRA'].drop(columns=['Male', 'Female'],axis=1) #["STATE/UT","Year","CAUSE","Total"]
#input_data_df_MH['Year'].apply(pd.to_datetime)
#print(input_data_df_MH.columns)
#print(input_data_df_MH.head())
number_of_years = input_data_df_MH['Year'].unique().tolist()
#print(number_of_years)
MH_Max_cases_per_year_df = pd.DataFrame()

for i in number_of_years:
    df = input_data_df_MH[input_data_df_MH['Year'] ==i]
    #print("min Total value = ",df['Total'].max())
    MH_Max_cases_per_year_df = MH_Max_cases_per_year_df.append(df[df['Total']==df['Total'].max()],ignore_index = True)
    df.drop(df[df.Total < 50].index,inplace=True)
    #print(df)
    explodeTuple = np.zeros(len(df))
    lst = list(explodeTuple)
    lst[0] = 0.15
    explodeTuple = tuple(lst)
    #print(explodeTuple)
    #colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E","#BE624E"]
    colors= ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','green','orange']
    # Create a pie chart
    plt.pie(
            # using data total)arrests
            df['Total'],
            # with the labels being officer names
            labels=df['CAUSE'],
            # with no shadows
            shadow=True,
            # with colors
            #colors=colors,
            # with one slide exploded out
            #explode=explodeTuple,
            # with the start angle at 90%
            startangle=90,
            radius=15,  labeldistance=1.0,
            # with the percent listed as a fraction
            autopct='%1.1f%%',
            rotatelabels = 120,
            counterclock=False
            )
    # View the plot drop above
    plt.axis('equal')
    # View the plot
    plt.tight_layout()
    plt.show()
    
print(MH_Max_cases_per_year_df)
