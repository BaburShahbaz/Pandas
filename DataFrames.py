# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 04:04:46 2024

@author: Babur Shahbaz
"""


## Create a Python code that generates random integers between 20 and 40, 
# reshapes them into a 5x4 NumPy array, and converts the array into a 
# Pandas DataFrame with custom row and column labels:
import numpy as np
import pandas as pd
np.random.seed(50)
a=np.random.randint(20,40,20).reshape(5,4)
print(a)
print()
df=pd.DataFrame(a,['R1','R2','R3','R4','R5'],['C1','C2','C3','C4'])
print(df)
print()
print()

print(df['C2'])
print()
print(df[['C1','C4']])
print()
print(df.loc['R1'])
print()


## Adding new column C5 which is the addition of C1 and C2
print(df)
print()
df['C5']=df['C1']+df['C2']
print(df)
print()

## Delete C5
x=df.drop('C5',axis=1)
print(x)
print(df)  ## C5 not deleted from df 
print()

df.drop('C5',axis=1,inplace=True)
print(df)
print()

## For Rows
## Adding new Row R6 which is the sum of R1 and R2
df.loc['R6']=df.loc['R1']+df.loc['R2']
print(df)
print()

## Deleting Row R6
df.drop('R6',inplace=True)
print(df)
print()

## Accessing the datasets
# Print the value R4-C3
print(df.loc['R4','C3'])
print(df.iloc[3,2])

## Please print a new df in which only R1 R5 and C3 and C4
x=df.loc[['R1','R5'],['C3','C4']]
print(x)


















