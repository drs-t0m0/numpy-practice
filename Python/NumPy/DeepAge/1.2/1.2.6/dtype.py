import numpy as np

a = np.array([0, 1, 2])
print(a.dtype)
print("-" * 30)

b = np.array([0, 1, 2], dtype='int32')
print(b.dtype)
print("-" * 30)

c = np.array([0, 1, 2], dtype='float')
print(c.dtype)
print("-" * 30)
print(c)
print("-" * 30)

d = np.array([3e50, 4e35], dtype='float64')
print(d.dtype)
print("-" * 30)

e = np.array([3.5, 4.2, -4.3], dtype='int')
print(e.dtype)
print("-" * 30)
print(e)
print("-" * 30)

f = np.array([0, 3, 0, -1], dtype='bool')
print(f.dtype)
print("-" * 30)
print(f)
print("#" * 30)

g = np.array([0., 1., 2.], dtype='int64')
print(g)
print("-" * 30)

g.dtype = 'int32'
print(g)
print("-" * 30)

g.dtype = 'float64'
print(g)
print("-" * 30)

g.dtype = 'float32'
print(g)
print("-" * 30)

g.dtype = 'int64'
print(g)
print("#" * 30)

h = np.random.randint(10, size=100, dtype='int8')
i = np.random.randint(10, size=100, dtype='int64')
print(h.nbytes)
print("-" * 30)
print(i.nbytes)
