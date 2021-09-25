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
        ans.append(np.average(T[rg*c:rg*c+rem]))
    return ans

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

def LCSS(T1, T2):
    pass
