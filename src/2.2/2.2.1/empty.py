import numpy as np
import time


def zeros():
    for i in range(10000):
        _ = np.zeros((1, i))


def empty():
    for i in range(10000):
        _ = np.empty((1, i))


start_time = time.time()
zeros()
print(time.time() - start_time)

start_time = time.time()
empty()
print(time.time() - start_time)
