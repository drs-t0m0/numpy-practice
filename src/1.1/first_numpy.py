import numpy as np

a = np.array([1, 2, 3])

# ブロードキャスト
print(a)
print("-" * 30)
print(a * 3)
print("-" * 30)
print(a + 2)

print("#" * 30)

b = np.array([2, 2, 0])

# アダマール積
print(a + b)
print("-" * 30)
print(a / b)
print("-" * 30)
print(a * b)

print("#" * 30)

# 内積
print(np.dot(a, b))

print("#" * 30)

# 等値配列
print(np.arange(10))
print("-" * 30)
print(np.arange(0, 10, 2))
print("-" * 30)
print(np.linspace(0, 10, 15))

print("#" * 30)

# 形状
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
print("-" * 30)
print(c.shape)

print("#" * 30)

d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
              [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
print(d)
print("-" * 30)
print(d.shape)

print("#" * 30)

# 和
print(np.sum(c))
print("-" * 30)
print(np.sum(c, axis=1))

print("#" * 30)

# 形状変化
print(c.reshape(3, 2))
print("-" * 30)
print(c.reshape(6, 1))

print("#" * 30)

# 転置
print(c.T)
print("-" * 30)
print(np.transpose(c))

print("#" * 30)

# 乱数
print(np.random.randn())
print("-" * 30)
print(np.random.rand())
print("-" * 30)
print(np.random.randn(2, 3))

print("#" * 30)

# インデックス
print(a)
print("-" * 30)
print(a[0])
print("-" * 30)
print(a[2])
print("-" * 30)

a[1] = 3
print(a)
print("-" * 30)
a[1] = 2
print(a)

print("#" * 30)

print(c)
print(c[0, 0])
print("-" * 30)
print(c[0, 2])
print("-" * 30)
print(c[1, 2])

print("#" * 30)

# スライシング
d = np.array([0, 5, 2, 7, 1, 9])
print(d[1:5])
print("-" * 30)
print(d[1:3])
print("-" * 30)
print(d[0:5:2])
print("-" * 30)
print(d[::-1])

print("#" * 30)

# ブロードキャスティング
print(a)
print("-" * 30)
print(c)
print("-" * 30)
print(a + c)
print("-" * 30)
print(a * c)

print("#" * 30)

# Numpyの高速演算

import time


def calculate_time():
    a = np.random.randn(100000)
    b = list(a)
    start_time = time.time()
    for _ in range(1000):
        sum_1 = np.sum(a)
    print("Using NumPy\t %f sec" % (time.time() - start_time))
    start_time = time.time()
    for _ in range(1000):
        sum_2 = sum(a)
    print("Not using NumPy\t %f sec" % (time.time() - start_time))


calculate_time()
