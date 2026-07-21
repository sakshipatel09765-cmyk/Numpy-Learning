#extact a subarray from an main array
#arr[start: stop : step]
#arr[1: 10 : 1] -> 10 exclude rehta h means stop pe jo element likhoge woh exclude rahega

import numpy as np

myarr = np.array([1,2,3,4,5,6,7,8,9,10])
print(myarr[1:5])  # -> from 1 to 5 index and last is exclude
print(myarr[:9])   # ->starts from 0 index if you not write
print(myarr[::2])  
print(myarr[::-1])