import numpy as np

print(np.amax(np.array([1, 2, 3, 2, 1])))
print("#" * 30)

arr = np.array([1, 2, 3, 4]).reshape((2, 2))
print(arr)
print("-" * 30)
print(np.amax(arr, axis=0))
print("-" * 30)
print(np.amax(arr, axis=1))
print("#" * 30)

print(np.amax(arr, keepdims=True))
