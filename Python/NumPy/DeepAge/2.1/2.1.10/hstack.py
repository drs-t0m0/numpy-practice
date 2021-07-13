import numpy as np

a = np.arange(12)
b = np.arange(2)

print(a)
print("-" * 30)
print(b)
print("-" * 30)

print(np.hstack((a, b)))
print("-" * 30)

c = np.arange(2).reshape(1, 2)
d = np.arange(5).reshape(1, 5)
print(d)
print("-" * 30)

print(np.hstack((c, d)))
print("#" * 30)

# 3次元の多次元配列
e = np.arange(12).reshape(2, 2, 3)
f = np.arange(6).reshape(2, 1, 3)

print(e)
print("-" * 30)
print(f)
print("-" * 30)

print(np.hstack((e, f)))
