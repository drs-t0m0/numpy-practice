import numpy as np

a = np.arange(12)
print(a)
print("-" * 30)

b = np.reshape(a, (3, 4))
print(b)
print("#" * 30)

# aにも変更が反映されている
b[0, 1] = 0
print(b)
print("-" * 30)
print(a)
print("#" * 30)

c = np.arange(12)
d = np.reshape(c, (3, 4,), order='C')
print(d)
print("-" * 30)

d = np.reshape(c, (3, 4), order='F')
print(d)
print("#" * 30)

a = np.arange(12).reshape((3, 4))
print(a)
print("-" * 30)

b = np.arange(12).reshape((3, -1))
print(b)
