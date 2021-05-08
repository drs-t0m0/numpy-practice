import numpy as np

a = np.random.randint(10, size=(2, 3))
print(a)
print("-" * 30)

print(np.any(a == 9))
print("-" * 30)

print(np.any(a == 5))
print("-" * 30)

# 行方向にみていく
print(np.any(a % 2 == 0, axis=0))
print("-" * 30)

# 列方向にみていく
print(np.any(a % 2 == 0, axis=1))
print("#" * 30)

print(np.any(a % 2 == 1, axis=1, keepdims=True))
print("-" * 30)

print(np.any(a > 2, keepdims=True))
print("#" * 30)

print((a % 5 == 0).any())
print("-" * 30)

print((a > 3).any())
print("-" * 30)

b = np.random.randint(10, size=(2, 3))
print(b)
print("-" * 30)

print((a == b).any())
print("-" * 30)

print((a == b).any(axis=1, keepdims=True))
