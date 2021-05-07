import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print("-" * 30)
print(a.ndim)
print("#" * 30)

a = np.arange(6).reshape((3, 2))
print(a)
print("-" * 30)
print(a.shape)
print("#" * 30)

b = np.array([a, a])
print(b.shape)
print("-" * 30)
print(b)
print("#" * 30)

print(b.sum(axis=0).shape)
print(b.sum(axis=0))
print("-" * 30)
print(b.sum(axis=1).shape)
print(b.sum(axis=1))
print("-" * 30)
print(b.sum(axis=2).shape)
print(b.sum(axis=2))
