#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[8]:



data = pd.read_csv("data.csv")
print(data,"\n")
d = np.array(data)[:,:-1]
print("Attributes : ",d)
target = np.array(data)[:,-1]
print("\n Target : ",target)
def findS(c,t):
    for i,val in enumerate(t):
        if val=="yes":
            sh = c[i].copy()
            break
    for i,val in enumerate(c):
        if t[i]=="yes":
            for x in range(len(sh)):
                if val[x] != sh[x]:
                    sh[x] = '?'
                else:
                    pass
    return sh
print("Final hypothesis: ",findS(d,target))


# In[ ]:



