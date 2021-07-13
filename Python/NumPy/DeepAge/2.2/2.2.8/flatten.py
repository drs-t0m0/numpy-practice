import numpy as np

# 2次元配列を1次元配列に変換
a = np.arange(10).reshape(2, 5)
print(a)
print("-" * 30)

b = a.flatten()
print(a)
print("-" * 30)
print(b)
print("-" * 30)
print(a.shape)
print("-" * 30)
print(b.shape)
print("#" * 30)

# 3次元配列を1次元配列に変換
c = np.arange(12).reshape(2, 2, 3)
print(c)
print("-" * 30)

d = c.flatten()
print(c)
print("-" * 30)
print(d)
print("-" * 30)
print(c.shape)
print("-" * 30)
print(d.shape)
