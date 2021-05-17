import numpy as np

a = np.array([1, 2])
b = np.array([4, 3])

# ２次元ベクトル同士の内積
print(np.dot(a, b))
print("-" * 30)

# ベクトルのノルムの２乗
print(np.dot(a, a))
print("#" * 30)

# ただの数字を入れてもその積が返される
print(np.dot(4, 5))
print("#" * 30)

# 複素数
c = np.array([1j, 2j])
d = np.array([4j, 3j])

print(np.dot(c, d))
print("-" * 30)
print(np.dot(a, d))
print("#" * 30)

e = np.matrix([1, 2])
f = np.matrix([[4], [3]])
print(np.dot(e, f))
print("#" * 30)

a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 3], [2, 1]])
print(np.dot(a, b))
print("-" * 30)
print(np.dot(b, a))
print("-" * 30)

c = np.arange(9).reshape((3, 3))
d = np.ones((3, 3))
print(np.dot(c, d))
print("#" * 30)

d = np.matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
e = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(np.dot(d, e))
print("#" * 30)

result = np.zeros((2, 2))
a = np.arange(4).reshape(2, 2)
b = np.ones((2, 2))
print(a)
print("-" * 30)

np.dot(a, b, out=result)
print(result)
print("-" * 30)

np.dot(b, a, out=result)
print(result)
