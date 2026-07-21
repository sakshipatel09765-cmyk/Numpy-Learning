# How numpy handles diffrent shapes of arrays
'''
rule 1: matching dimensions - [1,2,3] + [4,5,6] = [5,7,9]
'''
import numpy as np

matix = np.array([[1, 2, 3],[4,5,6]])  #2*3 matrix
vector = np.array([10,20,30])       #1D Array

result = matix + vector

print(result)

'''
Expanding single elements - [1,2,3] + [10] = [11,12,13]

'''

import numpy as np

arr1 = np.array([1, 2, 3])  
arr2 = np.array([10])       

result = arr1 + arr2

print(result)

'''
Icompatiable shapes - ERROR show karte h
'''
import numpy as np

arr1 = np.array([1, 2, 3])  
arr2 = np.array([10,20])  
result = arr1 + arr2

print(result)  

#solution - .reshape()

#ValueError: operands could not be broadcast together with shapes (3,) (2,) 