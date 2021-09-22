## Trajectory Data Analysis
- This is the course project for Duke University's Compsci 531D Fall21.

For part 1:
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
- from 3.1.3_Assignment import * (then you can use dtw and dfd in 3.1.3_Assignment.py)

Data structure:
- To change the data structure, for example, you want T1 in the shape of (2,n), simply use .T when you pass it into the function.
- If you need a different shape of the path/ want it as a list/ want it in a reverse order, you can call reshape, tolist, argsort.
- Feel free to change the code implementation, I'm totally fine with it!
