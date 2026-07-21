'''
np.concatenate((array1, array2), axis = 0)

'''
import numpy as np
arr1= np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
new_arr = np.concatenate((arr1, arr2), axis=0)      #agar ishmein axis nhi bhi likha toh kam chal jayega because ye 1-d array h
print(new_arr)
