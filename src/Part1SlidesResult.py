from Part1 import *
from tools import *
import numpy as np
import pandas
import matplotlib.pyplot as plt

# Data_Highway1 = pandas.read_csv("../data/highway.csv")

Data_Highway = read_trajectories("../data/highway.csv")


print('==================================================================================')
print('Getting the first pair of trajectories: T (id=5), T_prime(id=18) from the highway.csv dataset in lane 1...\n')

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

print('==================================================================================')
print('Getting the second pair of trajectories: T (id=28), T_prime(id=22) from the highway.csv dataset in lane 1...')

# next pair
T_28 = Data_Highway[481:496]
print('data for id=28:\n{:}\n'.format(T_28))

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

print('==================================================================================')
print('Step3: test the performance of dtw and dfd for speech recognition')
print('')
T_fast = pandas.read_csv("../data/voice/fast.csv")
T_shift_fast = pandas.read_csv("../data/voice/shift_fast.csv")
T_normal = pandas.read_csv("../data/voice/normal.csv")
T_shift_normal = pandas.read_csv("../data/voice/shift_normal.csv")

# six pair of tests for dtw
distance_dtw_1, path_dtw_1 = dtw(T_fast.to_numpy(), T_shift_fast.to_numpy())
distance_dtw_2, path_dtw_2 = dtw(T_fast.to_numpy(), T_normal.to_numpy())
distance_dtw_3, path_dtw_3 = dtw(T_fast.to_numpy(), T_shift_normal.to_numpy())
distance_dtw_4, path_dtw_4 = dtw(T_shift_fast.to_numpy(), T_normal.to_numpy())
distance_dtw_5, path_dtw_5 = dtw(T_shift_fast.to_numpy(), T_shift_normal.to_numpy())
distance_dtw_6, path_dtw_6 = dtw(T_normal.to_numpy(), T_shift_normal.to_numpy())


print('test 1 cost (dtw): {:}'.format(distance_dtw_1))
print('test 2 cost (dtw): {:}'.format(distance_dtw_2))
print('test 3 cost (dtw): {:}'.format(distance_dtw_3))
print('test 4 cost (dtw): {:}'.format(distance_dtw_4))
print('test 5 cost (dtw): {:}'.format(distance_dtw_5))
print('test 6 cost (dtw): {:}'.format(distance_dtw_6))

print('')

# six pair of tests for dfd
distance_dfd_1, path_dfd_1 = dfd(T_fast.to_numpy(), T_shift_fast.to_numpy())
distance_dfd_2, path_dfd_2 = dfd(T_fast.to_numpy(), T_normal.to_numpy())
distance_dfd_3, path_dfd_3 = dfd(T_fast.to_numpy(), T_shift_normal.to_numpy())
distance_dfd_4, path_dfd_4 = dfd(T_shift_fast.to_numpy(), T_normal.to_numpy())
distance_dfd_5, path_dfd_5 = dfd(T_shift_fast.to_numpy(), T_shift_normal.to_numpy())
distance_dfd_6, path_dfd_6 = dfd(T_normal.to_numpy(), T_shift_normal.to_numpy())

print('test 1 cost (dfd): {:}'.format(distance_dfd_1))
print('test 2 cost (dfd): {:}'.format(distance_dfd_2))
print('test 3 cost (dfd): {:}'.format(distance_dfd_3))
print('test 4 cost (dfd): {:}'.format(distance_dfd_4))
print('test 5 cost (dfd): {:}'.format(distance_dfd_5))
print('test 6 cost (dfd): {:}'.format(distance_dfd_6))
