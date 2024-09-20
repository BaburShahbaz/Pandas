# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 04:42:06 2024

@author: Babur Shahbaz
"""

import numpy as np
import pandas as pd
a={'A':[1.0,np.nan,np.nan],'B':[2.0,3.0,np.nan],'C':[4.0,5.0,6.0]}
b=pd.DataFrame(a)
print(b)
print()

## Drop Rows where Nan/missing values are present
x=b.dropna()
print(x)
print()
## Drop Columns where Nan/Missing values are present
y=b.dropna(axis=1)
print(y)
print()


## Thresh: value of thresh will print the rows
l=b.dropna(thresh=2)  ## print the row who have 2 non zero elements
print(l)
print()


## Fill : fill the value at Nan
m=b.fillna(value=9.0)
print(m)
print()


## fill the value 0f (2,B) by the mean of 2 and 3
n=b['B'].fillna(value=b['B'].mean())
print(n)
print()

o=b.fillna(value=b['B'].sum())
print(o)

