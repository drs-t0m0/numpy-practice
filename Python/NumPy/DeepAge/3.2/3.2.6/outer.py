import numpy as np

a = np.array([1, 2, 3, 2, 1])
b = np.array([0, 2, 4, 6, 8, 1])
print(np.outer(a, b))
print("-" * 30)

print(a.shape)
print("-" * 30)

print(b.shape)
print("-" * 30)

print(np.outer(a, b).shape)
print("-" * 30)

print(np.outer(a, b) == a.reshape(-1, 1) * b)
print("#" * 30)

b = b.reshape(2, -1)
c = np.random.randint(0, 5, size=(2, 4))
print(b)
print("-" * 30)
print(c)
print("-" * 30)

print(np.outer(b, c))
print("-" * 30)

print(np.outer(b.ravel(), c.ravel()))