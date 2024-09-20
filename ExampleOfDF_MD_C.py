# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 05:53:10 2024

@author: Babur Shahbaz
"""

import numpy as np
import pandas as pd
a={'A':[10,15,np.nan,20],'B':[np.nan, 25, 30, np.nan],'C':[35, np.nan, 40, 45],
   'D':[50, 55, 60, 65]}
## Assign row labels as 'Row1', 'Row2', 'Row3', 'Row4'. 
b=pd.DataFrame(a,['Row1','Row2','Row3','Row4'])
print(b)
print()
#  Drop all rows where at least one value is missing.
c=b.dropna()
print(c)
print()
# Drop all columns where at least one value is missing.
d=b.dropna(axis=1)
print(d)
print()
#  Fill all missing values with the mean of the corresponding column.
print(b)
print()
# e=b['Row1','B'].fillna(value=b['Row1','B'].mean())
# print(e)
# print()

# Select rows where the value in column 'A' is greater than 10.
e=b[b['A']>10]
print(e)
print()
# Select rows where the value in column 'C' is less than 40 and 
# the value in column 'D' is greater than 50.
f=b[(b['C']<40) & (b['D']>50)]
print(f)
print()
# Select rows where the value in column 'B' is NaN.
g=b[b['B']==np.nan]
print(g)




