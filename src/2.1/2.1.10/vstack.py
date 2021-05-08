import numpy as np

a = np.arange(12).reshape(-1, 1)
b = np.arange(2).reshape(-1, 1)

print(a)
print("-" * 30)
print(b)
print("-" * 30)

print(np.vstack((a, b)))
print("-" * 30)

c = np.arange(2).reshape(1, 2)
d = np.arange(4).reshape(2, 2)

print(c)
print("-" * 30)
print(d)
print("-" * 30)

print(np.vstack((c, d)))
print("#" * 30)

# 3次元配列
e = np.arange(24).reshape(4, 3, 2)
f = np.arange(6).reshape(1, 3, 2)

print(e)
print("-" * 30)
print(f)
print("-" * 30)

g = np.vstack((e, f))
print(g)
print("-" * 30)

print(g.shape)