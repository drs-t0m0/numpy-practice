import numpy as np

a = np.random.randint(0, 10, 20)
print(a)
print("-" * 30)

print(np.mean(a))
print("-" * 30)

b = a.reshape(4, 5)
print(b)
print("-" * 30)

# shapeを変更しても結果は変わらない
print(np.mean(b))
print("#" * 30)

# 行方向、つまり列ごとの平均を求めていく
print(np.mean(b, axis=0))
print("-" * 30)

# 列方向、つまり行ごとの平均を求めていく
print(np.mean(b, axis=1))
print("-" * 30)

c = np.random.rand(24).reshape((2, 3, 4))
print(c)
print("-" * 30)

print(np.mean(c, axis=0))
print("-" * 30)
print(np.mean(c, axis=1))
print("-" * 30)
print(np.mean(c, axis=2))
print("#" * 30)

d = np.random.rand(1000)
print(d.dtype)
print("-" * 30)

print(np.mean(d))
print("-" * 30)

print(np.mean(d, dtype="float32"))
print("-" * 30)
print(np.mean(d, dtype="float16"))
print("#" * 30)

print(b)
print("-" * 30)

e = np.mean(b, keepdims=True)
print(e)
print("-" * 30)
print(e.shape)
print("-" * 30)

f = np.mean(b, keepdims=False)
print(f)
print("-" * 30)

g = np.mean(b, axis=1, keepdims=True)
print(g)
print("-" * 30)
print(g.shape)
print("-" * 30)

h = np.mean(b, axis=1, keepdims=False)
print(h)
print("-" * 30)
print(h.shape)
