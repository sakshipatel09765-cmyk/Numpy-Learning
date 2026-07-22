 #1. np.isnan -> detect missing values

import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

# we cann't compare nan values directly

# print(np.isnan == np.isnan)
