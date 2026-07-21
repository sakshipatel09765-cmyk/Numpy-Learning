# insert in 2-D array

import numpy as np
arr_2D= np.array([[1,2,3],[4,5,6]])
# print(arr_2D)
new_arr = np.insert(arr_2D, 2, [5,6], axis=1)
print(new_arr)
new_arr2 = np.insert(arr_2D, 2, [5,6,7], axis=0)
print(new_arr2)
new_arr3 = np.insert(arr_2D, 2, [5,6], axis=None)
print(new_arr3)
