import numpy as np

a = np.random.randn(1200 * 1000).reshape(1200, -1)
np.save('a', a)
print(np.load('a.npy'))
print("-" * 30)

print(a.shape)
print("-" * 30)

b = np.load('a.npy')
print(b.shape)
print("-" * 30)

c = np.random.randn(12 * 20 * 40).reshape(12, 20, 40)
np.save('c', c)

d = np.load('c.npy')
print(d.shape)
