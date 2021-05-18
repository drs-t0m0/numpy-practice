import numpy as np


def zscore(x, axis=None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd = np.std(x, axis=axis, keepdims=True)
    zscore = (x - xmean) / xstd
    return zscore


a = np.random.randint(10, size=(2, 5))
print(a)
print("-" * 30)

print(zscore(a))
print("-" * 30)

print(zscore(a, axis=1))
print("-" * 30)

b = zscore(a, axis=1)
print(b.sum(axis=1))
print("-" * 30)

print(b.std(axis=1))
print("#" * 30)


def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x - min) / (max - min)
    return result


b = np.random.randint(10, size=(2, 5))
print(b)
print("-" * 30)

c = min_max(b)
print(c)
print("-" * 30)

d = min_max(b, axis=1)
print(d)
print("#" * 30)


def normalize(v, axis=-1, order=2):
    l2 = np.linalg.norm(v, ord=order, axis=axis, keepdims=True)
    l2[l2 == 0] = 1
    return v / l2


a = np.array([1, 2, 3, 2, 1])
b = normalize(a)
print(b)
print("-" * 30)

print((b * b).sum())
print("-" * 30)

c = np.random.randint(10, size=(3, 4))
print(c)
print("-" * 30)

d = normalize(c, axis=None)
print(d)
print("-" * 30)

print((d * d).sum())
print("-" * 30)

e = normalize(c, axis=1)
print(e)
print("-" * 30)

f = np.random.randint(10, size=(2, 3, 4))
print(normalize(f, axis=(1, 2)))
