# change dimension without changing or modifying its data
# arr.reshape(rows, columns)
#only done when its dimensions are match
import numpy as np
arr= np.array([1,2,3,4,5,6])
reshape_arr = arr.reshape(2,3)
print(reshape_arr)

# Reshaping does not create copy it return view


