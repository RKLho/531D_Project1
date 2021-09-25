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
        Data -> array of unstructed trajectories [[id1, x1, y1]...]

        Output:
        array of trajectories [[[x1, y1], [x2, y2]]..]
    """
    n = np.unique(Data[:,0])
    x=[Data[Data[:,0]==i,1:3] for i in n]
    return x