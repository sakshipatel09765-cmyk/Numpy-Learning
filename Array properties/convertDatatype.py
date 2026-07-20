# convert type of data type of array
import numpy as np
arr = np.array([1.2, 2.4, 3.5, 4.0])
arr = arr.astype(int)
print(arr)
print(arr.dtype)