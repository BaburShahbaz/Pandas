# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:25:33 2024

@author: Babur Shahbaz
"""

## Series with numpy array (Data) and Index/Label 
import numpy as np
import pandas as pd
a=np.array([10,20,30,40,50])
print(pd.Series(a))
print()
b=['a','b','c','d','e']
x=pd.Series(a,b)
print(x)
print()
print()
## Accessing data from series in data vs label
print(a[1])
print()
print(x['c'])
print()
print(x[['b','c']])
print()

## creating Series with dictionary
a={'a':10,'b':20,'c':30,'d':40,'e':50}
x=pd.Series(a)
print(x)
print()

## Accessing Data from a Series
print(x.iloc[1])  ## accessing by position
print()
print(x['a'])     ## accessing by label
print()
print(x[['b','d']]) ## acessing by multiple labels
print() 
print()



## Sum of 2 Series in data:labels
s1=pd.Series([10,20,30,40,50],['Ali','Saad','Omar','Usman','Babur'])
s2=pd.Series([5,10,15,20,25],['Ali','Zafar','Omar','Usman','Babur'])
s3=s1+s2
print(s3)
print()
print()


## Sum of 2 Series in dictionary
a=pd.Series({'a':10,'b':20,'c':30,'d':40,'e':50})
b=pd.Series({'a':10,'b':20,'c':30,'f':40,'e':50})
z=a+b
print(z)
print()
