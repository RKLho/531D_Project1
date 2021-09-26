# -*- coding: utf-8 -*-
"""PartTwo.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MVmkANj-j78fT3lb2EZGF87kCv8xQoYv
"""

import numpy as np
import pandas

def read_trajectories(path: str) -> 'ndarry':
  """Input:
     path -> string of the csv file path

     Output:
     ndarray with shape(x, y)

     import pandas and numpy are required
  """

  Data_temp = pandas.read_csv(path)
  return np.array(Data_temp)

def center_trajectories(traj_list: list, distance_func) -> "trajectories":
  """Input:
     traj_list -> ndarray of trajectories with shape(m, n, 4)
     m is the number of trajectories in this ndarray
     trajectories are represented by ndarray of shape (n, 4) where n represents 
     the number of points and 4 represents id, x, y, lane coordinates

     Output:
     ndarray with shape(n, 4)

     import pandas and numpy are required
  """
  #traj_list = traj_set.tolist(traj_set)
  traj_list_size = len(traj_list)
  distances = np.zeros(traj_list_size)

  for i in range(traj_list_size):
    for j in range(traj_list_size):
      distances[i] += distance_func(traj_list[i][:, 1:3], traj_list[j][:, 1:3])[0]
  
  return traj_list[np.argmin(distances)]

def n_average_trajectories(traj_list: list, h:int) -> "trajectories":
  """Input:
     traj_list -> ndarray of trajectories with shape(m, n, 4)
     m is the number of trajectories in this ndarray
     trajectories are represented by ndarray of shape (n, 4) where n represents 
     the number of points and 4 represents id, x, y, lane coordinates
    
     h -> the number of points representing the n average trajectories

     Output:
     ndarray with shape(h, 2)

     import pandas and numpy are required
  """
  #traj_list = traj_set.tolist(traj_set)
  traj_list_size = len(traj_list)

  h_average_traj = np.zeros((h, 2))

  for i in range(h):   
    curr_x_added = 0
    curr_y_added = 0
    for j in range(traj_list_size):
      arc_length = get_arc_length(traj_list[j])
      curr_x = (i+1) / h
      curr_remaining_arc_length = curr_x * arc_length
      #curr_remaining_arc_length = curr_x
      print("arc_lenth", curr_x, curr_remaining_arc_length)
      for p in range(len(traj_list[j]) - 1):
        #(traj_list[j][p][1] <= curr_x * ).all() and (traj_list[j][p+1][1] >= curr_x).all()
        line_seg_arc_length = np.sqrt(euclidean_square(traj_list[j][p][1:3], traj_list[j][p+1][1:3]))
        curr_remaining_arc_length -= line_seg_arc_length
        print("curr_remain", p, curr_remaining_arc_length)
        if curr_remaining_arc_length <= 1e-4 :

          curr_remaining_arc_length += line_seg_arc_length
          proportion = curr_remaining_arc_length / line_seg_arc_length
          #find the equation          
          coefficients = np.polyfit(traj_list[j][p:p+2, 1:3].T[0], traj_list[j][p:p+2, 1:3].T[1], 1)
          polynomial = np.poly1d(coefficients)
          #get the y value
          x1 = traj_list[j][p:p+2, 1:3].T[0][1]
          x2 = traj_list[j][p:p+2, 1:3].T[0][0]
          x_length = np.abs(x1 - x2)
          curr_x = np.minimum(x1, x2) + x_length*proportion
          curr_y_added += polynomial(curr_x)
          curr_x_added += curr_x
          print(curr_x_added)
          break
    
    curr_y_added = curr_y_added / traj_list_size
    curr_x_added = curr_x_added / traj_list_size
    h_average_traj[i][0] = curr_x_added
    h_average_traj[i][1] = curr_y_added
  
  return h_average_traj

def get_arc_length(trajectory) -> int:
  arc_length = 0
  for i in range(len(trajectory)-1):
    arc_length += np.sqrt(euclidean_square(trajectory[i][1:3], trajectory[i+1][1:3]))
  return arc_length
