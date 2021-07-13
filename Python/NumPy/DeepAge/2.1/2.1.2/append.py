import numpy as np
import time

a = [1, 2, 3]
a.append(2)
print(a)
print("-" * 30)

a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)
print("#" * 30)

# aの末尾に要素を追加
a = np.arange(12)
print(np.append(a, [6, 4, 2]))
print("-" * 30)

b = np.arange(12).reshape((3, 4))
print(b)
print("-" * 30)

# axisを指定しないと一次元配列が返ってくる
print(np.append(b, [1, 2, 3, 4]))
print("#" * 30)

print(b)
print("-" * 30)
print(np.append(b, [[12, 13, 14, 15]], axis=0))
print("#" * 30)

c = np.arange(12).reshape((3, 4))
print(c)
print("-" * 30)

d = np.linspace(0, 26, 12).reshape(3, 4)
print(d)
print("-" * 30)

# 行方向に追加
print(np.append(c, d, axis=0))
print("-" * 30)

# 列方向に要素が追加
print(np.append(c, d, axis=1))
print("#" * 30)


# 速度比較
def np_append():
    a = np.array([1, 2, 3])
    for i in range(10000):
        a = np.append(a, [i])
    return a


def list_append():
    a = [1, 2, 3]
    for i in range(10000):
        a.append(i)
    return np.array(a)

start_time = time.time()
np_append()
print(time.time() - start_time)
print("-" * 30)

# Pythonのlistの方が高速
start_time = time.time()
list_append()
print(time.time() - start_time)
