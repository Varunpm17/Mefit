#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:35:49 2020

@author: vm and gm 
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('MFGD.csv',usecols=['Machine No.','Date', 'Transaction Amount'])
#csv_input = input("Enter slot machine csv file: ")
df2 = pd.read_csv("/Users/varunmeduri/Desktop/MeFit/drive_download/ReadySpaces.csv")

key = df2.iat[0,0]

RowCount = len(df.index)
ColumnCount = len(df.columns)

RowCount2    = len(df2.index)
ColumnCount2 = len(df2.columns)

df = df[df["Machine No."] == key]

aggregation_functions = {'Transaction Amount': 'sum'}
df = df.groupby(df['Date']).aggregate(aggregation_functions).reset_index()

df.plot(x='Date',y='Transaction Amount',kind='bar',figsize=(10,10),title=key)
plt.show()

