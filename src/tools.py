import numpy as np
import pandas
import matplotlib.pyplot as plt

def draw_assignment(T1, T2, path_assignment, title, save_path):
    """Input:
        T1, T2 -> pair of trajectories
        path_assignment -> monotone assignment

        Output:
        None

        import pandas, numpy and matplotlib.pyplot are required
    """
    plt.figure()

    plt.plot(T1[:,0], T1[:,1], 'k', linewidth=1)
    plt.scatter(T1[:,0], T1[:,1], s=10, c='k')
    plt.plot(T2[:,0], T2[:,1], 'r', linewidth=1)
    plt.scatter(T2[:,0], T2[:,1], s=10, c='r')

    for i in range(len(path_assignment)):
        T1_node = path_assignment[i][0]
        T2_node = path_assignment[i][1]
        # print(T1_node, T2_node)
        plt.plot([T1[T1_node][0], T2[T2_node][0]], [T1[T1_node][1], T2[T2_node][1]], 'k--', linewidth=0.5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.savefig(save_path)
    plt.show()

    return
    
def read_trajectories(path: str) -> 'ndarry':
    """Input:
        path -> string of the csv file path

        Output:
        ndarray with shape(x, y)

        import pandas and numpy are required
    """
    Data_temp = pandas.read_csv(path)
    return np.array(Data_temp)

def reconstruct(Data):
    """Input:
     Data -> array of unstructed trajectories [[id, x, y]...]

     Output:
     array of trajectories [T1, T2, ...]

    """
    n = np.unique(Data[:,0])
    list = []
    for i in n:
        list.append(Data[Data[:,0]==i, 1:3])
    list = np.array(list, dtype=object)
    return list
