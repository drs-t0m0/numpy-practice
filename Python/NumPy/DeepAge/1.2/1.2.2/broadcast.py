import numpy as np

# ブロードキャスト
print(np.array([[1, 2, 3]]) + [1])
print("#" * 30)

# ルール1
a = np.array([[1, 2]])
print(a.shape)
print("-" * 30)
b = np.array([3, 4])
print(b.shape)
print("-" * 30)
print(a + b)  # b(2,)を(1, 2)に変換して計算
print("#" * 30)

# ルール4
a = np.array([1, 2])
b = np.array([[3, 4], [2, 3]])
print(a)
print("-" * 30)
print(b)
print("-" * 30)
print(a.shape)
print("-" * 30)
print(b.shape)
print("-" * 30)
print(a + b)
print("#" * 30)

a = np.array([[2], [1]])
b = np.array([5])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a)
print("-" * 30)
print(b)
print("-" * 30)
print(c)
print("-" * 30)
print(a.shape)
print("-" * 30)
print(b.shape)
print("-" * 30)
print(c.shape)
print(a + b + c)
