import numpy as np
import time

start_time = time.time()
np.zeros(10000)
print(time.time() - start_time)

start_time = time.time()
np.empty(10000)
print(time.time() - start_time)

start_time = time.time()
np.ones(10000)
print(time.time() - start_time)
