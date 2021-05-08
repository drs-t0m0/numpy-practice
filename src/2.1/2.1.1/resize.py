import numpy as np

a = np.arange(12)

print(np.reshape(a, (3, 4)))
print("-" * 30)

# 配列のサイズが要素数より大きいと繰り返される
print(np.resize(a, (3, 5)))
print("-" * 30)

# 逆に配列のサイズが小さいと、元のデータが使用されない
print(np.resize(a, (3, 2)))
print("#" * 30)

# aには変更が反映されていない
b = np.resize(a, (3, 4))
b[0, 1] = 0
print(b)
print("-" * 30)
print(a)
print("#" * 30)

a.resize((3, 5), refcheck=False)
print(a)
print("-" * 30)

# bにもcの変更が反映されている。
b = np.arange(12)
c = b
c.resize((3, 4))
print(c)
print("-" * 30)
print(b)

