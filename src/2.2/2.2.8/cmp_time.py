import numpy as np
import time

arr = np.repeat(5, 10000).reshape(250, 40)

start_time = time.time()
arr.flatten()
print(time.time() - start_time)

start_time = time.time()
np.ravel(arr)
print(time.time() - start_time)
