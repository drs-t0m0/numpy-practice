import numpy as np

a = np.array([10, 20, 12, 0, 3, 5])
print(np.var(a))
print("#" * 30)

b = np.random.randint(20, size=(3, 4))
print(b)
print("-" * 30)

print(np.var(b))
print("-" * 30)

# 行ごとの分散を求める
print(np.var(b, axis=0))
print("-" * 30)

# 列ごとの分散を求める
print(np.var(b, axis=1))
print("-" * 30)

# こうすると0,1番目の軸方向でやるとすべての範囲の分散を求める
print(np.var(b, axis=(0, 1)))
print("#" * 30)

c = np.random.randn(100).reshape(5, 20)
print(c.dtype)
print("-" * 30)

print(c)
print("-" * 30)

print(np.var(c, dtype='float32'))
print("-" * 30)

print(np.var(c, dtype='float64'))
print("#" * 30)

d = np.random.randn(10)
print(d)
print("-" * 30)

# まずはデフォルトの値であるddof=0(標本分散)から
print(np.var(d, ddof=0))
print("-" * 30)

# 次は不偏分散を求める
print(np.var(d, ddof=1))
print("-" * 30)

e = np.random.randn(5)

print(e)
print("-" * 30)

print(np.var(e))
print("-" * 30)

print(np.var(e, ddof=1))
print("#" * 30)

f = np.random.randint(20, size=(2, 5, 10))
print(f)
print("-" * 30)

f_var = np.var(f, axis=1)
print(f_var.shape)
print("-" * 30)

f_var = np.var(f, axis=1, keepdims=True)
print(f / f_var)
