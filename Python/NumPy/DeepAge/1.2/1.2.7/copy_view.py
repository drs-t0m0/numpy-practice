import numpy as np

# viewは同じメモリを参照しているため
# viewにあたる配列の要素が変更されると
# 元の配列にも変更が反映される
a = np.array([1, 2, 3])
d = a.view()
d[0] = 100
print(d)
print("-" * 30)
print(a)
print("#" * 30)

# copyだと変更は反映されない
c = a.copy()
c[1] = 25
print(c)
print("-" * 30)
print(a)
print("#" * 30)

# 代入
a = np.array([1, 2, 3])
b = a
print(id(a) == id(b))
print("-" * 30)

c = a[:]
print(id(a) == id(c))
print("-" * 30)

c[1] = 22
print(a)
print("-" * 30)

d = a[:1]
print(id(a) == id(d))
print("-" * 30)

d[0] = 11
print(a)
print("-" * 30)
print(d)
print("#" * 30)

e = a.copy()
print(e.base is a)
print("-" * 30)

e[2] = 234
print(e)
print("-" * 30)
print(a)
print("#" * 30)

# 演算
a = np.array([1, 2, 3])
c = a
a = a + 1
print(c)
print("-" * 30)
print(a)
print("#" * 30)

a = np.array([1, 2, 3])
c = a
a += 1
print(c)
print("-" * 30)
print(a)
print("#" * 30)

a = np.array([1, 2, 3])
c = a
print(np.add(a, 1, out=a))
print("-" * 30)
print(a)
print("-" * 30)
print(c)
print("#" * 30)


def test():
    import time
    X = np.ones(100000000, dtype='int8')
    Y = np.ones(100000000, dtype='int8')
    a = time.time()
    for _ in range(100):
        X = X * 4 + Y * 3
        X = np.ones(100000000, dtype='int8')
    b = time.time()
    print('X = X*4 + Y*3: {} sec'.format((b - a) / 100))
    a = time.time()
    for _ in range(100):
        X *= 4
        X += Y * 3
        X = np.ones(100000000, dtype='int8')
    b = time.time()
    print('X *= 4; X += Y*3: {} sec'.format((b - a) / 100))
    a = time.time()
    for _ in range(100):
        np.multiply(X, 4, out=X)
        np.multiply(Y, 3, out=Y)
        np.add(X, Y, out=X)
        X = np.ones(100000000, dtype='int8')
    b = time.time()
    print("using functions: {} sec".format((b - a) / 100))


# test()
print("#" * 30)

# 配列の一次元化
a = np.random.randn(2, 3, 9)
b = a.ravel()
c = a.flatten()
print(a)
print("-" * 30)
a[0, 0, 0] = 129
print((a[0, 0, 0], b[0], c[0]))
print("#" * 30)

# fancy indexing
a = np.random.randint(10, size=100)
print(a)
print("-" * 30)

n = a % 3 == 0
print(n)
print("-" * 30)

print(a[n])
print("-" * 30)

k = a[n]
print(np.may_share_memory(a, k))
print("-" * 30)

f = a[np.arange(0, 10, 2)]
print(np.may_share_memory(a, f))
print("#" * 30)

# may_share_memory関数
a = np.array([1, 2, 3])
b = a
c = a
d = a.copy()
print(np.may_share_memory(a, b))
print("-" * 30)
print(np.may_share_memory(a, c))
print("-" * 30)
print(np.may_share_memory(a, d))
print("-" * 30)
print(np.shares_memory(a, b))
print("-" * 30)
print(np.shares_memory(a, d))
