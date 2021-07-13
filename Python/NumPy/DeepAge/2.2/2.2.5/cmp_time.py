import numpy as np
import time

start_time = time.time()
np.eye(10000)
print(time.time() - start_time)

start_time = time.time()
np.identity(10000)
print(time.time() - start_time)
