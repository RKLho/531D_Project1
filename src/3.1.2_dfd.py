#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# (x1, y1) is the coordinate for p1, and (x2, y2) is the coordinate for p2
# this func returns the Euclidean distance between p1 and p2
def Euclidean(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def dfd(T1, T2):
    n = len(T1)
    m = len(T2)
    
    ca = np.ones((n, m))*-1
    
    def _c(i, j):
        if ca[i][j] > -1:
            ca[i][j] = ca[i][j]
        elif i == 0 and j == 0:
            ca[i][j] = Euclidean(T1[0, :], T2[0, :])
        elif i > 0 and j == 0:
            ca[i][j] = max(_c(i-1, 0), Euclidean(T1[i, :], T2[0, :]))
        elif i == 0 and j > 0:
            ca[i][j] = max(_c(0, j-1), Euclidean(T1[0,:], T2[j,:]))
        elif i > 0 and j > 0:
            ca[i][j] = max(min(_c(i-1,j), _c(i-1,j-1),_c(i,j-1)), Euclidean(T1[i, :], T2[j, :]))
        else:
            ca[i][j] = np.inf
        return ca[i][j]
    
    return _c(n-1, m-1)


# In[3]:


x = np.array([[1.0,1.0], [2.0,2.0], [3.0,3.0], [4.0,4.0], [5.0,5.0]])
y = np.array([[2.0,2.0], [3.0,3.0], [4.0,4.0]])

my_distance_dfd = dfd(x, y)
print(my_distance_dfd)

