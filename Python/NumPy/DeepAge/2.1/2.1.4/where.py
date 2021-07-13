import numpy as np

a = np.arange(20, 0, -2)

print(a)
print("-" * 30)

print(np.where(a < 10))
print("-" * 30)
print(a[np.where(a < 10)])
print("#" * 30)

# 多次元配列
a = np.arange(12).reshape((3, 4))

print(a)
print("-" * 30)

print(np.where(a % 2 == 0))
print("#" * 30)

# 三項演算子
print(np.where(a % 2 == 0, 'even', 'odd'))
print("-" * 30)

b = np.reshape(a, (3, 4))
c = b ** 2

print(c)
print("-" * 30)

print(np.where(b % 2 == 0, b, c))
print("#" * 30)

print(np.where(b % 2 == 0, b, (10, 8, 6, 4)))