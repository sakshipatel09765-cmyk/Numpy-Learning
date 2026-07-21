'''
np.delete(array, index, axis=None)
new array return and original remain unchanged
'''

import numpy as np
arr= np.array([1,2,3,4])
newarr= np.delete(arr, 3, axis=None)
print(newarr)