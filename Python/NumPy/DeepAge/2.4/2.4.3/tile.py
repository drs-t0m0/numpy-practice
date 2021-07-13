import numpy as np

a = np.array([0, 1, 2])

# 1次元配列を２回繰り返す。
print(np.tile(a, 2))
print("-" * 30)

# 3×2の二次元配列の要素がaになっているイメージ
print(np.tile(a, (3, 2)))
print("-" * 30)

print(np.tile(a, (2, 3, 4)))
print("-" * 30)

b = np.arange(6).reshape(2, 3)
print(np.tile(b, 2))
print("-" * 30)

print(np.tile(b, (2, 3)))
print("-" * 30)

print(np.tile(b, (2, 1, 1)))
print("#" * 30)

c = np.random.rand(10)
b = np.array([0, 1, 0, 2, 1])
b = np.tile(b, 2)
print(c * b)
