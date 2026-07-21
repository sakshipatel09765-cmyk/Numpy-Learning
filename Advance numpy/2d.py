import numpy as np
arr_2D= np.array([[1,2,3],[4,5,6]])

newarr = np.delete(arr_2D, 0, axis=1)
print(newarr)