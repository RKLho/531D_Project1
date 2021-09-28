from Part1 import *
from tools import *
import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer

Data_Highway1 = pandas.read_csv("../data/highway.csv")

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
distance_dtw_pair_1, path_dtw_pair_1 = dtw(T_5[:, 1:3], T_18[:, 1:3])
print('The dynamic time warping (DTW) cost is: {:}'.format(
    distance_dtw_pair_1))
print('The associated monotone assignment C is:\n{:}\n'.format(
    path_dtw_pair_1))

# get the cost and assignment for the first pair
distance_dfd_pair_1, path_dfd_pair_1 = dfd(T_5[:, 1:3], T_18[:, 1:3])
print('The discrete Fréchet distance (DFD) cost is: {:}'.format(
    distance_dfd_pair_1))
print('The associated monotone assignment C is:\n{:}\n'.format(
    path_dfd_pair_1))

# draw results for first path
draw_assignment(T_5[:, 1:3], T_18[:, 1:3], path_dtw_pair_1, 'dtw (id=5, id=18, cost={:})'.format(
    distance_dtw_pair_1), '../images/part1/dtw_5_18')
draw_assignment(T_5[:, 1:3], T_18[:, 1:3], path_dfd_pair_1, 'dfd (id=5, id=18, cost={:})'.format(
    distance_dfd_pair_1), '../images/part1/dfd_5_18')

print('==================================================================================')
print('Getting the second pair of trajectories: T (id=28), T_prime(id=22) from the highway.csv dataset in lane 1...')

# next pair
T_28 = Data_Highway[481:496]
print('data for id=28:\n{:}\n'.format(T_28))

T_22 = Data_Highway[374:390]
print('data for id=22:\n{:}\n'.format(T_22))
#
# get the cost and assignment for the first pair
distance_dtw_pair_2, path_dtw_pair_2 = dtw(T_28[:, 1:3], T_22[:, 1:3])
print('The dynamic time warping (DTW) cost is: {:}'.format(
    distance_dtw_pair_2))
print('The associated monotone assignment C is:\n{:}\n'.format(
    path_dtw_pair_2))

# get the cost and assignment for the first pair
distance_dfd_pair_2, path_dfd_pair_2 = dfd(T_28[:, 1:3], T_22[:, 1:3])
print('The discrete Fréchet distance (DFD) cost is: {:}'.format(
    distance_dfd_pair_2))
print('The associated monotone assignment C is:\n{:}\n'.format(
    path_dfd_pair_2))
#
# # draw results for first path
draw_assignment(T_28[:, 1:3], T_22[:, 1:3], path_dtw_pair_2, 'dtw (id=28, id=22, cost={:})'.format(
    distance_dtw_pair_2), '../images/part1/dtw_28_22')
draw_assignment(T_28[:, 1:3], T_22[:, 1:3], path_dfd_pair_2, 'dfd (id=28, id=22, cost={:})'.format(
    distance_dfd_pair_2), '../images/part1/dfd_28_22')

print('==================================================================================')
print('Step3: test the performance of dtw and dfd for speech recognition')

def compare_wav(wav1,  wav2, dtw_results, dfd_results):
    # Read data and normalize such that the maximum amplitude is 1
    T1 = pandas.read_csv("../data/voice/"+wav1+".csv")
    T2 = pandas.read_csv("../data/voice/"+wav2+".csv")
    T1 = T1.to_numpy()
    T2 = T2.to_numpy()

    transformer = Normalizer().fit(np.vstack((T1,T2)))
    T1 = transformer.transform(T1)
    T2 = transformer.transform(T2)

    # DTW vs DFD
    dtw_dist, dtw_path = dtw(T1, T2)
    dfd_dist, dfd_path = dfd(T1, T2)
    comparison = "{} vs {}".format(wav1, wav2)
    dtw_results[comparison] = dtw_dist
    dfd_results[comparison] = dfd_dist
    return dtw_results, dfd_results


dtw_results = {}
dfd_results = {}
dtw_results, dfd_results = compare_wav(
    "unshifted_slow", "unshifted_fast", dtw_results, dfd_results)
dtw_results, dfd_results = compare_wav(
    "unshifted_slow", "shifted_slow", dtw_results, dfd_results)
dtw_results, dfd_results = compare_wav(
    "unshifted_slow", "shifted_fast", dtw_results, dfd_results)
dtw_results, dfd_results = compare_wav(
    "unshifted_fast", "shifted_slow", dtw_results, dfd_results)
dtw_results, dfd_results = compare_wav(
    "unshifted_fast", "shifted_fast", dtw_results, dfd_results)
dtw_results, dfd_results = compare_wav(
    "shifted_slow", "shifted_fast", dtw_results, dfd_results)

print("")
print("DTW:")
for k, v in sorted(dtw_results.items(), key=lambda item: item[1]):
    print("{:>40} has cost {}".format(k, v))

print("")
print("DFD:")
for k, v in sorted(dfd_results.items(), key=lambda item: item[1]):
    print("{:>40} has cost {}".format(k, v))
