# we use it when we want to convert multi-D array to 1-D array
#.ravel()  -> view  -> original array ko modify karega
#.flatten() -> copy     -> does not disturb array

import numpy as np
arr_2D= np.array([[1,2,3],[4,5,6]])

print(arr_2D.ravel())
print(arr_2D.flatten())