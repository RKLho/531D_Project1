#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# (x1, y1) is the coordinate for p1, and (x2, y2) is the coordinate for p2
# this func returns the euclidean_square distance between p1 and p2
def euclidean_square(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

# T1, T2 are trajectories
def dtw(T1, T2):
    n = len(T1)
    m = len(T2)
    # use dynamic programming
    my_matrix = np.zeros((n+1, m+1))

    for i in range(n+1):
        for j in range(m+1):
            my_matrix[i, j] = np.inf
    my_matrix[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = euclidean_square(T1[i-1,:], T2[j-1,:])
            index_min = np.argmin([my_matrix[i-1][j-1], my_matrix[i-1][j], my_matrix[i][j-1]])
            if index_min == 0:
                my_matrix[i][j] = cost + my_matrix[i-1][j-1]
            elif index_min == 1:
                my_matrix[i][j] = cost + my_matrix[i-1][j]
            else:
                my_matrix[i][j] = cost + my_matrix[i][j-1]
    warp_path = findPath(my_matrix)

    return my_matrix[n][m], warp_path


def findPath(my_matrix):
    # index starts from 0
    i, j = np.array(my_matrix.shape) - 2
    path = np.array([i, j])
    while i > 0 or j > 0:
        index = np.argmin((my_matrix[i, j], my_matrix[i, j + 1], my_matrix[i + 1, j]))
        if index == 0:
            i = i-1
            j = j-1
        elif index == 1:
            i = i-1
        else:
            j = j-1
        path = np.vstack([path, np.array([i, j])])

    return path

def dfd(T1, T2):
    n = len(T1)
    m = len(T2)

    # -1 as unvisited
    my_matrix = np.ones((n, m))*-1

    def search(i, j):
        # if already visited, return the value
        if my_matrix[i][j] > -1:
            my_matrix[i][j] = my_matrix[i][j]
        elif i == 0 and j == 0:
            my_matrix[i][j] = euclidean_square(T1[0, :], T2[0, :])
        elif i > 0 and j == 0:
            my_matrix[i][j] = max(search(i-1, 0), euclidean_square(T1[i, :], T2[0, :]))
        elif i == 0 and j > 0:
            my_matrix[i][j] = max(search(0, j-1), euclidean_square(T1[0,:], T2[j,:]))
        elif i > 0 and j > 0:
            my_matrix[i][j] = max(min(search(i-1,j), search(i-1,j-1),search(i,j-1)), euclidean_square(T1[i, :], T2[j, :]))
        return my_matrix[i][j]

    return search(n-1, m-1), findDfdPath(my_matrix)

def findDfdPath(my_matrix):
    n, m = my_matrix.shape
    # pad to reuse findPath
    pad_m = np.hstack([np.ones((n,1))*np.inf, my_matrix])
    pad_m = np.vstack([np.ones((1,m+1))*np.inf, pad_m])

    path = findPath(pad_m)

    return path
