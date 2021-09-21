#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# (x1, y1) is the coordinate for p1, and (x2, y2) is the coordinate for p2
# this func returns the Euclidean distance between p1 and p2
def Euclidean(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# # T1, T2 are trajectories
def dtw(T1, T2):
    n = len(T1)
    m = len(T2)
    my_matrix = np.zeros((n+1, m+1))
    
    for i in range(n+1):
        for j in range(m+1):
            my_matrix[i, j] = np.inf
    my_matrix[0][0] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = Euclidean(T1[i-1,:], T2[j-1,:])
            my_matrix[i][j] = cost + min(my_matrix[i-1][j], my_matrix[i][j-1], my_matrix[i-1][j-1])
    
        
    return my_matrix[n][m]


# In[3]:


x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3], [4,4]])
my_distance_dtw = dtw(x, y)
print(my_distance_dtw)

