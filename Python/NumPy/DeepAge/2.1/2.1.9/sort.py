import numpy as np

a = np.random.randint(0, 100, size=20)
print(a)
print("-" * 30)

print(np.sort(a))
print("#" * 30)

values = [('Alice', 25, 9.7), ('Bob', 12, 7.6), ('Catherine', 1, 8.6), ('David', 10, 7.6)]
dtype = [('name', 'S10'), ('ID', int), ('score', float)]
a = np.array(values, dtype=dtype)

print(np.sort(a, order='score'))
print("-" * 30)
print(np.argsort(a, order='score'))
print("#" * 30)

print(np.sort(a, order=['score', 'ID']))
print("-" * 30)
print(np.argsort(a, order=['score', 'ID']))
print("#" * 30)

b = np.random.randint(0, 100, size=20).reshape(4, 5)
print(b)
print("-" * 30)

# axisを指定しないと列方向の中でソート
print(np.sort(b))
print("-" * 30)

print(np.argsort(b))
print("-" * 30)

print(np.sort(b, axis=0))
print("-" * 30)

print(np.argsort(b, axis=0))
print("#" * 30)

c = np.random.randint(0, 100, size=(2, 4, 5))
print(c)

print(np.sort(c, axis=0))
print("-" * 30)

print(np.argsort(c, axis=0))
print("#" * 30)

a = np.random.randint(0, 100, 20)
print(a)
print("-" * 30)

print(np.sort(a))
print("-" * 30)

print(a)
print("-" * 30)

a.sort()
print(a)
print("-" * 30)
