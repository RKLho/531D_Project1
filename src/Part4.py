import tools
import numpy as np


# # T1, T2 are trajectories
def pdtw(T1, T2):
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