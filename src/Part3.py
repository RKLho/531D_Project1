import numpy as np
from Part1 import *
from Part2 import *

""" function get_alltrajlist(input_set):
input:[N,4]darray
    output: a list consists of m [n,4] darray
    m is the number of trajectories
    n is the number of points of each trajectory """
def get_alltrajlist(input_set):
    N=len(input_set)
    t_id=input_set[0][0]
    # split_list is a list of locations to split ndarray into each trajectory
    split_list=[]
    all_traj_list=[]
    for j in range(N):
        t_id_cur=input_set[j][0]
        if(t_id_cur != t_id):
            split_list.append(j)
            t_id = t_id_cur
    all_traj_list=np.split(input_set,split_list)
    return all_traj_list

""" function get_partition(all_traj_list,k)
    input: 
    all_traj_list:the output of function get_alltrajlist, a list of trajectories, m*n*4
    k:the number of needed clusters k 
    output: 
    partition: random generated k clusters
"""
def get_partition(all_traj_list,k):
    m=len(all_traj_list)
    # step 1: randomly partition X into k sets
    #partition: a list of k lists which represents a set of trajectories
    # step 1.1: to ensure none of clusters are empty, firstly randomly put one trajectory in each cluster
    partition=[]
    traj_partitioned=set()
    for iter in range(k):
        traj_i_random=np.random.randint(0,m)
        while(traj_i_random in traj_partitioned):
            traj_i_random=np.random.randint(0,m)
        partition.append([all_traj_list[traj_i_random]])
        traj_partitioned.add(traj_i_random)
    # step 1.2: for each trajectory(not partitioned before), uniformly randomly choose a cluster of k clusters
    for j in range(m):
        if(j in traj_partitioned):
            continue
        # generates random integer from 0 to k-1
        set_i= np.random.randint(0,k)
        partition[set_i].append(all_traj_list[j])
    return partition

""" function find_mincluster(input_set, dist_func, k, r, tmax)
    input:
    input_set:[N,4] ndarray
    dist_func: the distance function of two trajectores
    k: the number of k-clusters
    r: the number of rounds
    tmax: for each round, the maximum times of center computation and re-assigment
    output:
    min_cost: the minimum cost of k-clusters
    arg_min_cost: the partition whose cost is the min_cost
"""
#def center_trajectories(traj_list: list, distance_func) -> "trajectories":
def find_mincluster(input_set, dist_func, k, r, tmax):
    # input_set is a [N,4] ndarray
    # all_traj_list is a list consisting of m trajectories, every trajectory is a [n,4] ndarray
    all_traj_list=get_alltrajlist(input_set)
    m=len(all_traj_list)
    for i in range(r):
        # step 1: randomly partition X into k sets
        #partition a list of k lists which represents a set of trajectories
        partition=get_partition(all_traj_list,k)
        min_cost=np.Inf
        # step 2: repeat the process of center computation and Re-assignment
        for t in range(tmax):
            #center_trajectory: a list of all the center_trjectories in k sets, each one is a [n,4] ndarray 
            # if cluster_same keeps the True, then break the loop
            cluster_same=True
            center_trajectory=[]
            cost_process=0
            for iter in range(k):
                center_trajectory.append(center_trajectories(partition[iter],dist_func))
            for p_i in range(k):
                partition_cur=partition[p_i]
                center_cur=center_trajectory[p_i]
                len_partition_cur=len(partition_cur)
                traj_i=0
                while(traj_i < len_partition_cur):
                    #for each trajectory
                    # arg_min_dist: the index of the center_trajectory which is the nearest to the trajectory
                    # initialize arg_min_dist as the current index of partition where the trajectory is 
                    # min_dist: the smallest distance between the trajectory and center trajectories
                    min_dist=dist_func(partition_cur[traj_i][:,1:3],center_cur[:,1:3])[0]
                    arg_min_dist=p_i
                    for center_i in range(k):
                        if(center_i == p_i):
                            continue
                        dist=dist_func(partition_cur[traj_i][:,1:3],center_trajectory[center_i][:,1:3])[0]
                        if(dist<min_dist):
                            # find a closer center, change the min and arg_min
                            cluster_same=False
                            min_dist=dist
                            arg_min_dist=center_i
                    # if a closer center is found, need to do re-assignment
                    if(arg_min_dist!=p_i):
                        partition[arg_min_dist].append(partition_cur[traj_i])
                        partition_cur.pop(traj_i)
                        len_partition_cur-=1
                    else:
                        traj_i+=1
                    cost_process+=min_dist
            if(cluster_same):
                break
        cost=calcu_cost(partition,center_trajectories,dist_func,k)
        if(cost<min_cost):
            min_cost=cost
            arg_min_cost=partition
    return min_cost, arg_min_cost

""" function calcu_cost(partition,center_func, dist_func,k)
    input:
    partition: a partition, a list of k lists, each list consists of some [n,4] ndarray(trajectory)
    center_func:the function to calculate the center trajectory of a cluster
    dist_func:the function to calculate the distance between two trajectories
    k:number of k-cluster
    output:the cost of the partition
"""                     
def calcu_cost(partition,center_func, dist_func,k):
    cost=0
    for p_i in range(k):
        partition_cur=partition[p_i]
        center_cur=center_func(partition_cur,dist_func)
        for traj_i in range(len(partition_cur)):
            cost+=dist_func(partition_cur[traj_i][:,1:3],center_cur[:,1:3])[0]
    return cost

# N=len(input_set)
    # leftover=input_set
    # t_id=input_set[0][0]
    # all_traj_list=[]
    # for j in range(N):
    #     t_id_cur=input_set[j][0]
    #     if(t_id_cur != t_id):
    #         traj,leftover=np.split(leftover,[j])
    #         all_traj_list.append(traj)
    #         t_id = t_id_cur

    # for traj_i in range(m):
            #     min_dist=np.inf
            #     for center_i in range(k):
            #         #input are both (n,4)
            #         dist=dist_func(all_traj_list[traj_i],center_trajectory(center_i))

            #         if(min_dist<dist):
            #             min_dist=dist

""" def get_partition(all_traj_list,k):
    m=len(all_traj_list)
    # step 1: randomly partition X into k sets
    #partition a list of k lists which represents a set of trajectories
    partition=[]
    for iter in range(k):
        partition.append([])
    for j in range(m):
        # generates random integer from 0 to k-1
        set_i= np.random.randint(0,k)
        partition[set_i].append(all_traj_list[j])
    return partition """
