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

def reconstruct(Data):
    """Input:
     Data -> array of unstructed trajectories [[id, x, y]...]

     Output:
     array of trajectories [T1, T2, ...]

    """
    n = np.unique(Data[:,0])
    x=[Data[Data[:,0]==i,1:3].tolist() for i in n]
    return x