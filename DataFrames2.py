# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 02:14:13 2024

@author: Babur Shahbaz
"""

## Conditional Selection
# import numpy as np
# import pandas as pd
# np.random.seed(50)
# a=np.random.randint(10,40,20).reshape(5,4)
# print(a)
# print()

# ## convert to dataframe
# b=pd.DataFrame(a,['R1','R2','R3','R4','R5'],['C1','C2','C3','C4'])
# print(b)

# ## Boolean Indexing
# print()
# print(b[b>15]) ## print all the values > 15 and print NaN for < 15
# print()
# print(b>15)  ## print True and False 
# print()
# print(b)
# print()
# print(b['C1']>15) ## Return True for C1>15 and False for <15
# print()
# print(b[b['C1']>15])  ## Return Values of True only
# print()
# print(b)
# print()
# print(b[b['C4']==15])
# print()
# print(b)
# print(b[b['C1']>15]['C2'])
# print()
# print()
# print()




################## 
import numpy as np
import pandas as pd
np.random.seed(50)
a=np.random.randint(1,28,20).reshape(5,4)
print(a)
print()
b=pd.DataFrame(a,['R1','R2','R3','R4','R5'],['C1','C2','C3','C4'])
print(b)
print()

## conditional selection
print(b>15)              ## True/False on dataframe
print()

print(b[b>15])           ## Return values in dataframes (True=Value) & (False=NaN) 
print()

print(b['C2']<15)        ## Return (R1 & R2 = True) and (R3,R4,R5 = False) with only C2
print()


print(b[b['C3']<10])     ## Return the only values < 10 from C3 
print()
print(a)
print()
print(b)
print()


print(b[b['C1']<5]['C2'])  ## It will check C1 < 5 on which rows and print C2 on that rows
print()


## Multiple Conditions
print(b)
print()
x=b[(b['C1']<5) & (b['C4']==6)]
print(x)
print()
y=b[(b['C1']<5) | (b['C4']==6)]
print(y)
print()


print(b)
print()
print(b.reset_index())
print()
print()
print()

## create a new column C5 name city 
a='Islamabad Lahore Peshawar Murree Karachi'.split()
print(a)
print()
b['City']=a
print(b)
print()
b.set_index('City',inplace=True)
print(b)

























