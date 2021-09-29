# Trajectory Data Analysis
- This is the course project for Duke University's Compsci 531D Fall21.

### Required Packages:
- numpy
- pandas
- matplotlib.pyplot
- sklearn.preprocessing

### Part 1:

Description:
- cost, path = dtw(T1, T2) takes in two trajectories T1 (nx2) and T2 (mx2) which are two sets of points that define polygonal curves,
  each row represents one point in R^2. See project 1 descriptions for more details to the definition of cost and path for dynamic time warping.

- cost, path = dfd(T1, T2) takes in two trajectories T1 (nx2) and T2 (mx2) which are two sets of points that define polygonal curves,
  each row represents one point in R^2. See project 1 descriptions for more details to the definition of cost and path for discrete Fréchet distance.

- path returned by dtw(T1, T2) and dfd(T1, T2) is a 2D array, the first column contains point i from T1 and the second column represents point j
  from T2. Here is one example:
  path = [[4 2]
          [3 2]
          [2 1]
          [1 0]
          [0 0]]
  [4 2] means the 4th point in T1 connects to 2nd in T2, etc.

Usage:
- from Part1 import * (then you can use dtw and dfd in Part1.py)
- Run 'python Part1Demo.py' for slides results

Data structure:
- To change the data structure, for example, you want T1 in the shape of (2,n), simply use .T when you pass it into the function.
- If you need a different shape of the path/ want it as a list/ want it in a reverse order, you can call reshape, tolist, argsort.

### Part 2:

Description:
- read_trajectories(path) takes string as the path of the csv file and return a ndarray with corresponding shape to store the data.

- center_trajectories(traj_list: list, distance_func) takes list/ndarray as the list contains trajectories and a distance function, return the center trajectory from the list     of trajectories. Shapes and details can be found in the comments

- n_average_trajectories(traj_list: list, h:int) takes list/ndarray as the list contains trajectories and an int as the average degree, return the averaged trajectory from the   list of trajectories. Shapes and details can be found in the comments

Usage:
- Part2.py includes just all the three functions

- Part2Demo.py/Part2DemoNotebook.ipynb includes all the three functions and some of my demo/test codes to display and verify. It can be used as an illustration on how these   functions work. Recommend open Part2DemoNotebook.ipynb on google colab if what to test out.

### Part 3:

Description:

* find_mincluster(all_traj_list, center_func, dist_func, k, r, tmax,h=0) takes in the list of all trajectories, a function to calculate the center trajectory, a function to calculate distances between two trajectories, the number of clusters, the number of rounds, the maximum times of re-assignment, the chosen h to calculate the center trajectory.

  It returns the minimum cost of partitions, and the partition whose cost is minimum.

* calcu_cost(partition,center_func, dist_func,k,h)takes in a partition, a function to calculate the center trajectory, a function to calculate the distance between two trajectories, the number of clusters, and the chosen h.

  It returns the cost of the partition.

* plot_cluster(partition,k,r)takes in a partition, the number of clusters, and the number of rounds

  It plots and saves figures of k-clusters

* get_partition(all_traj_list,k)takes in a list of trajectories and the number of clusters, and returns the randomly partitioned k-clusters

* get_alltrajlist(input_set)takes in a [N,4] ndarray which contains all trajectories, and returns a list consists of all trajectories(m,n,4), m is the number of trajectories, n is the number of points in each trajectory

Usage:

- Part3.py includes all functions, from Part3 import * (then you can use functions in Part3.py)

### Part 4:

Description:
- paa(T, c): PAA cuts a trajectory T of size n into N = n/c pieces. For each piece i, it computes the average point Pi as representative point.

- pdtw(T1, T2, c): Aggregate trajectory with ```paa``` function. Compute the distance and path with ```dtw``` function.

- paa(T:list, c): PAA cuts a trajectory T of size n into N = n/c pieces. For each piece i, it computes the average point Pi as representative point.

- pdtw(T1: list, T2: list, c): Aggregate trajectory with ```paa``` function. Compute the distance and path with ```dtw``` function.

- lcssDist(T1: list, T2: list): Use longest common subsequence algorithm to calculate distance and path between two trajectories T1 and T2. The distance is inversely proportional to the similarity of two trajectories.

Usage:
- from Part4 import * (then you can use paa, pdtw and lcssDist in Part4.py)
- The specific usage example including the visualization method are described and executed in Part4Demo.py
