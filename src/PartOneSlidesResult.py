from PartOne import *
from PartTwo import *
import numpy as np
import pandas
import matplotlib.pyplot as plt

Data_Highway1 = pandas.read_csv("../data/highway.csv")

Data_Highway = read_trajectories("../data/highway.csv")
#
print('Shape of data: {:}'.format(Data_Highway.shape))

print('Getting first pair of trajectories: T (id=5), T_prime(id=7) from the highway.csv dataset in lane 1...')

# id=5
T_5 = Data_Highway[91:107]
print('data for id=5:\n{:}\n'.format(T_5))

# id=7
T_7 = Data_Highway[125:143]
print('data for id=5:\n{:}\n'.format(T_7))

# get the cost and assignment for the first pair
distance_dtw_pair_1, path_dtw_pair_1 = dtw(T_5[:,1:3], T_7[:,1:3])
print('The dynamic time warping cost is: {:}'.format(distance_dtw_pair_1))
print('The associated monotone assignment C is:\n{:}'.format(path_dtw_pair_1))
