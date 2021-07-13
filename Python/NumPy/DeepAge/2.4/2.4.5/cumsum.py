import numpy as np

a = np.random.randint(10, size=20)
print(a)
print("-" * 30)

# まずは普通に足し合わせてみる
print(np.cumsum(a))
print("-" * 30)

# この形でもok
print(a.cumsum())
print("#" * 30)

print(np.cumsum(a, dtype='float32'))
print("-" * 30)

print(a.cumsum(dtype='float32'))
print("-" * 30)

b = np.random.rand(3, 4) * 10

c = np.random.randint(10, size=10, dtype='int8')
print(c)
print("-" * 30)

print(c.cumsum())
print("-" * 30)

print(c.cumsum().dtype)
print("-" * 30)

d = c.cumsum(dtype='int8')
print(d.dtype)
print("#" * 30)

print(b)
print("-" * 30)

print(np.cumsum(b))
print("-" * 30)

print(np.cumsum(b, axis=1))
print("-" * 30)

print(b.cumsum(axis=1))
print("-" * 30)

print(np.cumsum(b, axis=0))
print("-" * 30)

print(b.cumsum(axis=0))