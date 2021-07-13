import numpy as np

a = np.random.randint(0, 10, size=(2, 5))
print(a)
print("-" * 30)

print(np.sum(a))
print("-" * 30)

b = np.array([2, 4, 1, 6])
print(np.sum(b))
print("-" * 30)

c = np.random.randint(0, 10, size=(2, 4, 5))
print(c)
print("-" * 30)

print(np.sum(c))
print("#" * 30)

print(a)
print("-" * 30)

# 行方向に足し合わせる
print(np.sum(a, axis=0))
print("-" * 30)

# 列方向に足し合わせる
print(np.sum(a, axis=1))
print("-" * 30)

print(c)
print("-" * 30)

print(np.sum(c, axis=0))
print("-" * 30)
print(np.sum(c, axis=1))
print("-" * 30)
print(np.sum(c, axis=2))
print("#" * 30)

print(np.sum(c, axis=0, keepdims=True))
print("-" * 30)
print(np.sum(c, axis=1, keepdims=True))
print("-" * 30)
print(np.sum(c, axis=2, keepdims=True))
print("#" * 30)

print(np.sum(a, dtype='int8'))
print("-" * 30)
print(np.sum(a, axis=0, dtype='float'))
print("#" * 30)

print(a)
print("-" * 30)
print(b)
print("-" * 30)
print(c)
print("-" * 30)

print(a.sum())
print("-" * 30)
print(b.sum())
print("-" * 30)
print(c.sum())
print("-" * 30)

print(a.sum(axis=0))
print("-" * 30)
print(c.sum(axis=0))
print("-" * 30)
print(c.sum(axis=2))
print("-" * 30)

print(a.sum(axis=0, keepdims=True))
print("-" * 30)
print(c.sum(axis=2, keepdims=True))
print("-" * 30)

print(a.sum(axis=0, dtype='float'))
