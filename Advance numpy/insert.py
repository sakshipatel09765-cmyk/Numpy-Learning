"""
np.insert(array, index, value, asixNone)
array - original array
axis - is it is None then it will inserted into a flatten array
axis - 0 (rowwise)
asix - 1 (columnwise insert)

"""
import numpy as np
arr= np.array([1,2,3,4])
print(arr)
new_arr = np.insert(arr,2,4)
print(new_arr)

