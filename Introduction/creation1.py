#with default values
#np.zeroes(shape) (3) for 1D array, (3,3) for 2D array

import numpy as np
zeroes_array = np.zeros((3))
print(zeroes_array)


#one(shape)
ones_array = np.ones((3))
print(ones_array)

#full(shape, fill_value)
import numpy as np
full_array = np.full((3,3), 5)
print(full_array)