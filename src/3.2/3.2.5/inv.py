import numpy as np

a = np.random.randint(-9, 10, size=(2, 2))
print(a)
print("-" * 30)

# 逆行列
print(np.linalg.inv(a))
print("-" * 30)

# 積をとって単位行列
print(np.dot(a, np.linalg.inv(a)))
print("#" * 30)

b = np.random.randint(-10, 10, size=(3, 3))
print(b)
print("-" * 30)

c = np.linalg.inv(b)
print(c)
print("-" * 30)

print(np.dot(b, c))
print("-" * 30)
print(np.dot(c, b))
print("#" * 30)

d = np.random.randint(-10, 10, size=(4, 3, 3))
print(d)
print("-" * 30)

e = np.linalg.inv(d)
print(e)
print("-" * 30)

print(np.dot(d, e))
