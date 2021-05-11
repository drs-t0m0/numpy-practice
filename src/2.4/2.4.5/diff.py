import numpy as np

a = np.array([1, 2, 4, 1, 6, 8, 3])

print(np.diff(a, n=1))
print("-" * 30)
print(np.diff(a, n=2))
print("-" * 30)
print(np.diff(a, n=3))
print("-" * 30)
print(np.diff(a, n=4))
print("#" * 30)

b = np.random.randint(10, size=(5, 5))
print(b)
print("-" * 30)

# axis=1と同じ意味
print(np.diff(b, axis=-1))
print("-" * 30)

# 次は行方向
print(np.diff(b, axis=0))
print("-" * 30)

print(np.diff(b, axis=1, n=2))
print("#" * 30)
