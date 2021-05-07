import numpy as np

# start:stop:step
a = np.arange(15)
print(a)
print("-" * 30)
print(a[5:11:2])
print("#" * 30)

a = np.arange(10)
print(a)
print("-" * 30)
print(a[1:5])
print("-" * 30)
print(a[2:8:2])
print("-" * 30)
print(a[::-1])
print("-" * 30)
print(a[:3])
print("-" * 30)
print(a[4:])
print("-" * 30)
print((a[:3], a[3:]))
print("-" * 30)
print(a[::2])
print("-" * 30)
print(a[:])
print("#" * 30)

# 多次元
b = np.arange(20).reshape(4, 5)
print(b)
print("-" * 30)
print(b[1:3, 2:4])
print("-" * 30)
print(b[:2, 1:])
print("-" * 30)
print(b[::2, :])
print("-" * 30)
print(b[:, ::2])
print("-" * 30)
print(b[:, ::-1])
print("-" * 30)
print(b[::-1, ::-1])
print("#" * 30)

c = np.zeros((3, 4, 5))
print(c)
print("-" * 30)

c[1:, 1:4, :] = 1
print(c)
print("-" * 30)

c = np.zeros((3, 4, 5))
c[:, 1:2, 3:] = 1
print(c)
print("-" * 30)

c = np.zeros((3, 4, 5))
c[:, :, ::2] = 1
print(c)
print("-" * 30)

c = np.zeros((3, 4, 5))
c[::2, ::2, ::2] = 1
print(c)
