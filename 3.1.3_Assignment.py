#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# (x1, y1) is the coordinate for p1, and (x2, y2) is the coordinate for p2
# this func returns the Euclidean distance between p1 and p2
def Euclidean(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# T1, T2 are trajectories
def dtw(T1, T2):
    n = len(T1)
    m = len(T2)
    my_matrix = np.zeros((n+1, m+1))
    
    for i in range(n+1):
        for j in range(m+1):
            my_matrix[i, j] = np.inf
    my_matrix[0][0] = 0
#     path = np.array([1, 1])
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = Euclidean(T1[i-1,:], T2[j-1,:])
            index_min = np.argmin([my_matrix[i-1][j], my_matrix[i][j-1], my_matrix[i-1][j-1]])
            if index_min == 0:
                my_matrix[i][j] = cost + my_matrix[i-1][j]
            elif index_min == 1:
                my_matrix[i][j] = cost + my_matrix[i][j-1]
            else:
                my_matrix[i][j] = cost + my_matrix[i-1][j-1]
    warp_path = findPath(my_matrix)
    
    return my_matrix[n][m], warp_path

def findPath(my_matrix):
    n, m = my_matrix.shape
    i = n-1
    j = m-1

    path = np.array([i, j])
    
    while i > 1 or j > 1:
        if i == 1:
            path = np.vstack([path, np.array([i, j-1])])
            j = j-1
        elif j == 1:
            path = np.vstack([path, np.array([i-1, j])])
            i = i-1
        else:
            index_min = np.argmin([my_matrix[i-1][j], my_matrix[i-1][j-1], my_matrix[i][j-1]])
            if index_min == 0:
                path = np.vstack([path, np.array([i-1, j])])
                i = i-1
            elif index_min == 1:
                path = np.vstack([path, np.array([i-1, j-1])])
                j = j-1
                i = i-1
            else:
                path = np.vstack([path, np.array([i, j-1])])
                j = j-1
    
    return path-1


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
    
    return _c(n-1, m-1), findDfdPath(ca)

def findDfdPath(my_matrix):
    n, m = my_matrix.shape
    # pad
    pad_m = np.hstack([np.ones((n,1))*np.inf, my_matrix])
    pad_m = np.vstack([np.ones((1,m+1))*np.inf, pad_m])
    
    path = findPath(pad_m)
    
    return path


# In[3]:


x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3], [4,4]])
my_distance_dtw, my_path_dtw = dtw(x, y)
print(my_distance_dtw)
print(my_path_dtw)


# In[4]:


my_distance_dfd, my_path_dfd = dfd(x, y)
print(my_distance_dfd)
print(my_path_dfd)


# In[ ]:





# In[ ]:




