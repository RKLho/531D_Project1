from Part1 import *
from tools import *
import numpy as np
import pandas
import matplotlib.pyplot as plt
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

Data_Highway1 = pandas.read_csv("../data/highway.csv")

Data_Highway = read_trajectories("../data/highway.csv")
#
print('Shape of data: {:}'.format(Data_Highway.shape))

print('Getting first pair of trajectories: T (id=5), T_prime(id=7) from the highway.csv dataset in lane 1...')

# id=5
T_5 = Data_Highway[91:107]
print('data for id=5:\n{:}\n'.format(T_5))

# id=16
T_16 = Data_Highway[276:291]
print('data for id=16:\n{:}\n'.format(T_16))

# get the cost and assignment for the first pair
distance_dtw_pair_1, path_dtw_pair_1 = dtw(T_5[:,1:3], T_16[:,1:3])
print('The dynamic time warping (DTW) cost is: {:}'.format(distance_dtw_pair_1))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dtw_pair_1))

# distance, path = fastdtw(T_5[:,1:3], T_16[:,1:3], dist=euclidean)
# print(path)
# print(distance)

# get the cost and assignment for the first pair
distance_dfd_pair_1, path_dfd_pair_1 = dfd(T_5[:,1:3], T_16[:,1:3])
print('The discrete Fréchet distance (DFD) cost is: {:}'.format(distance_dfd_pair_1))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dfd_pair_1))

# draw results for first path
draw_assignment(T_5[:,1:3], T_16[:,1:3], path_dtw_pair_1, 'dtw (id=5, id=16)', '../images/part1/dtw_5_16')
draw_assignment(T_5[:,1:3], T_16[:,1:3], path_dfd_pair_1, 'dfd (id=5, id=16)', '../images/part1/dfd_5_16')

# next pair
T_18 = Data_Highway[308:323]
print('data for id=18:\n{:}\n'.format(T_5))

T_22 = Data_Highway[374:390]
print('data for id=22:\n{:}\n'.format(T_16))
#
# get the cost and assignment for the first pair
distance_dtw_pair_2, path_dtw_pair_2 = dtw(T_18[:,1:3], T_22[:,1:3])
print('The dynamic time warping (DTW) cost is: {:}'.format(distance_dtw_pair_2))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dtw_pair_2))


# get the cost and assignment for the first pair
distance_dfd_pair_2, path_dfd_pair_2 = dfd(T_18[:,1:3], T_22[:,1:3])
print('The discrete Fréchet distance (DFD) cost is: {:}'.format(distance_dfd_pair_2))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dfd_pair_2))
#
# # draw results for first path
draw_assignment(T_18[:,1:3], T_22[:,1:3], path_dtw_pair_2, 'dtw (id=18, id=22)', '../images/part1/dtw_18_22')
draw_assignment(T_18[:,1:3], T_22[:,1:3], path_dfd_pair_2, 'dfd (id=18, id=22)', '../images/part1/dfd_18_22')
