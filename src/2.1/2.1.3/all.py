import numpy as np

a = np.array([
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
])

print(np.all(a))
print("-" * 30)

b = np.ones((3, 3))
print(np.all(b))
print("-" * 30)
print(np.all(a < 2))
print("-" * 30)
print(np.all(b % 3 < 2))
print("#" * 30)

# 行方向にみていく
print(np.all(a, axis=0))
print("-" * 30)

# 列方向にみていく
print(np.all(a, axis=1))
print("-" * 30)

a[2, 0] = 0
print(a)
print("-" * 30)

print(np.all(a, axis=0))
print("#" * 30)

print(np.all(a, axis=0, keepdims=True))
print("#" * 30)

print(a.all())
print("-" * 30)
print(b.all())
print("-" * 30)
print(a.all(axis=1))
print("-" * 30)
print((a < 2))
print("-" * 30)
print(a.all(keepdims=True))
