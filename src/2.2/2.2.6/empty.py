import numpy as np

print(np.empty(10))
print("-" * 30)
print(np.empty((2, 3)))
print("#" * 30)

print(np.empty(5, dtype=np.int8))
print("-" * 30)
print(np.empty(10, dtype=np.bool))
print("-" * 30)
print(np.empty(10, dtype=complex))
