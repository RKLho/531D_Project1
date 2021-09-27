import numpy as np
import Part1

def paa(T, c):
    """
        Input:
        T -> array of points in trajectory with size n 
        c -> int: aggregate factor, aggregate T into N = n/c pieces

        Output:
        ans -> array: aggregated trajectory

        Piecewise aggregate approximation:
        PAA cuts a trajectory T of size n into N = n/c pieces. For each piece i, 
        it computes the average point Pi as representative point
    """
    if c > len(T) or c < 1:
        raise Exception("Aggregate Factor should be between 1 and len(T)")
    ans = []
    rg = int(len(T)/c)
    rem = len(T)%c
    for idx in range(rg):
        ans.append(np.average(T[idx*c:(idx+1)*c], axis=0))
    if rem>0:
        ans.append(np.average(T[rg*c:rg*c+rem], axis=0))
    return np.array(ans)

def pdtw(T1, T2, c):
    """
        Input:
        T1, T2 -> array of points in trajectory with size m, n
        c -> int: aggregate factor,

        Piecewise dynamic time warping operates on PAA
    """
    sT1 = paa(T1, c)
    sT2 = paa(T2, c)
    dist_matrix, warp_path=Part1.dtw(sT1, sT2)
    
    return dist_matrix, warp_path

def getDelta(m, n):
    return 0.5 * min(m, n)
    
def getEpsilon(T1:list):
    epsilonX = 0.1 * (np.max(T1[:,0]) - np.min(T1[:,0]))
    epsilonY = 0.1 * (np.max(T1[:,1]) - np.min(T1[:,1]))
    return epsilonX, epsilonY
    
def lcssDist(T1: list, T2: list) -> int:
    
    m = len(T1)
    n = len(T2)
    # delta = getDelta(m, n)
    avgYDiff = abs(np.average(T1[:,1]) - np.average(T2[:,1]))
    avgXDiff = abs(np.average(T1[:,0]) - np.average(T2[:,0]))
    epsilonX, epsilonY = getEpsilon(T1)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for col in range(len(T2)):
        for row in range(len(T1)):
            # print(abs(abs(T1[row][0] - T2[col][0])), epsilonX, abs(abs(T1[row][1] - T2[col][1]) - avgYDiff), epsilonY)
            if abs(abs(T1[row][0] - T2[col][0]) - avgXDiff) < epsilonX \
            and abs(abs(T1[row][1] - T2[col][1]) - avgYDiff) < epsilonY:
                matrix[row+1][col+1] = 1 + matrix[row][col]
            else:
                matrix[row+1][col+1] = max(matrix[row + 1][col], matrix[row][col + 1])
    # print(np.array(matrix))
    path = findPath(np.array(matrix))
    return matrix[m][n], path

def findPath(my_matrix):
    m, n = my_matrix.shape
    i = m - 1
    j = n - 1
    path = []

    while i >= 1 and j >= 1:
        index_min = np.argmax([my_matrix[i-1][j-1],my_matrix[i-1][j],my_matrix[i][j-1]])
        if index_min == 0:
            if(my_matrix[i-1][j-1]<my_matrix[i][j]):
                path.append([i-1, j-1])
            j = j-1
            i = i-1
        elif index_min == 1:
            i = i-1
        else:
            j = j-1

    return np.array(path)

