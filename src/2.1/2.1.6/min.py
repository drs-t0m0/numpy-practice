import numpy as np

a = np.array([
    [1.2, 1.3, 0.1, 1.5],
    [2.1, 0.2, 0.3, 2.0],
    [0.1, 0.5, 0.5, 2.3]
])

print(a.min())
print("-" * 30)
print(a.min(axis=0))
print("-" * 30)
print(a.min(axis=1))
print("-" * 30)
print(a.min(axis=0, keepdims=True))
print("-" * 30)
print(a.min(axis=1, keepdims=True))
