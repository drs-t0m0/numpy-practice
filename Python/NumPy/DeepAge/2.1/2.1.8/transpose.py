import numpy as np

# 二次元配列
a = np.arange(12).reshape(3, 4)
print(a)
print("-" * 30)

print(a.transpose())
print("-" * 30)

# 軸の順番を指定
print(a.transpose(1, 0))
print("-" * 30)

print(a.transpose(0, 1))
print("#" * 30)

# 一次元配列
b = np.arange(6)
print(b)
print("-" * 30)

# 軸が１つしかないので、特に変化は起こらない
print(b.transpose())
print("-" * 30)

print(b.shape)
print("-" * 30)

b = b.reshape(1, 6)
print(b)
print("-" * 30)

print(b.transpose())
print("#" * 30)

# 三次元配列
c = np.arange(24).reshape(4, 3, 2)
print(c)
print("-" * 30)

# (2,1,0)の配列
print(c.transpose())
print("-" * 30)

print(c.transpose(1, 0, 2))
print("#" * 30)

print(np.transpose(c))
print("-" * 30)

print(c.shape)
print("-" * 30)

print(np.transpose(c).shape)
print("-" * 30)

print(np.transpose(c, (1, 0, 2)))
print("-" * 30)

print(np.transpose(c, (1, 0, 2)).shape)
print("#" * 30)

b = np.arange(6)
print(b)
print("-" * 30)

print(np.transpose(b))
print("-" * 30)

b = b.reshape(1, 6)
print(b)
print("-" * 30)

print(np.transpose(b))
print("#" * 30)

print(a)
print("-" * 30)

print(a.T)
print("-" * 30)

print(b)
print("-" * 30)

print(b.T)
print("-" * 30)

print(c)
print("-" * 30)

print(c.T)
print("-" * 30)

print(a.transpose().shape == a.T.shape)
print("-" * 30)
print(b.transpose().shape == b.T.shape)
print("-" * 30)
print(c.transpose().shape == c.T.shape)
