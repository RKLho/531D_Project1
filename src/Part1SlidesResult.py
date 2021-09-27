from Part1 import *
from tools import *
import numpy as np
import pandas
import matplotlib.pyplot as plt

# Data_Highway1 = pandas.read_csv("../data/highway.csv")

Data_Highway = read_trajectories("../data/highway.csv")
#
print('Shape of data: {:}'.format(Data_Highway.shape))

print('Getting first pair of trajectories: T (id=5), T_prime(id=16) from the highway.csv dataset in lane 1...')

# id=5
T_5 = Data_Highway[91:107]
print('data for id = 5:\n{:}\n'.format(T_5))

# id=18
T_18 = Data_Highway[308:323]
print('data for id = 18:\n{:}\n'.format(T_18))

# get the cost and assignment for the first pair
distance_dtw_pair_1, path_dtw_pair_1 = dtw(T_5[:,1:3], T_18[:,1:3])
print('The dynamic time warping (DTW) cost is: {:}'.format(distance_dtw_pair_1))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dtw_pair_1))

# get the cost and assignment for the first pair
distance_dfd_pair_1, path_dfd_pair_1 = dfd(T_5[:,1:3], T_18[:,1:3])
print('The discrete Fréchet distance (DFD) cost is: {:}'.format(distance_dfd_pair_1))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dfd_pair_1))

# draw results for first path
draw_assignment(T_5[:,1:3], T_18[:,1:3], path_dtw_pair_1, 'dtw (id=5, id=18, cost={:})'.format(distance_dtw_pair_1), '../images/part1/dtw_5_18')
draw_assignment(T_5[:,1:3], T_18[:,1:3], path_dfd_pair_1, 'dfd (id=5, id=18, cost={:})'.format(distance_dfd_pair_1), '../images/part1/dfd_5_18')




# next pair
T_28 = Data_Highway[481:496]
print('data for id=18:\n{:}\n'.format(T_28))

T_22 = Data_Highway[374:390]
print('data for id=22:\n{:}\n'.format(T_22))
#
# get the cost and assignment for the first pair
distance_dtw_pair_2, path_dtw_pair_2 = dtw(T_28[:,1:3], T_22[:,1:3])
print('The dynamic time warping (DTW) cost is: {:}'.format(distance_dtw_pair_2))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dtw_pair_2))

# get the cost and assignment for the first pair
distance_dfd_pair_2, path_dfd_pair_2 = dfd(T_28[:,1:3], T_22[:,1:3])
print('The discrete Fréchet distance (DFD) cost is: {:}'.format(distance_dfd_pair_2))
print('The associated monotone assignment C is:\n{:}\n'.format(path_dfd_pair_2))
#
# # draw results for first path
draw_assignment(T_28[:,1:3], T_22[:,1:3], path_dtw_pair_2, 'dtw (id=28, id=22, cost={:})'.format(distance_dtw_pair_2), '../images/part1/dtw_28_22')
draw_assignment(T_28[:,1:3], T_22[:,1:3], path_dfd_pair_2, 'dfd (id=28, id=22, cost={:})'.format(distance_dfd_pair_2), '../images/part1/dfd_28_22')
