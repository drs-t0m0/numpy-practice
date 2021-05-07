import numpy as np

a = np.array([5, 3, 8, 9])
print(a)
print("-" * 30)
print(a.shape)
print("#" * 30)

b = a.reshape((2, 2))
print(b)
print("-" * 30)
print(b.shape)
print("#" * 30)

a.shape = (4, 1)
print(a)
print("-" * 30)

c = np.arange(12).reshape((3, 4))
print(c)
print("-" * 30)
c.shape = (1, 12)
print(c)
print("#" * 30)

a = np.array([1, 2, 3, 4, 5])
print(a.shape)
print("-" * 30)
b = np.array([[1], [2], [3], [4], [5]])
print(b.shape)
