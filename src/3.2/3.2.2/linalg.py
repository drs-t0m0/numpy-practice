import numpy as np
import numpy.linalg as LA

a = np.array([[2, 3], [4, -1]])
print(a)
print("-" * 30)

print(LA.det(a))
print("-" * 30)

b = np.array([[1, 1], [2, 2]])
print(b)
print("-" * 30)

print(LA.det(b))
print("#" * 30)

c = np.array([[1 - 1j, 3j], [-3j, 1 + 2j]])
print(c)
print("-" * 30)

print(LA.det(c))
print("#" * 30)

d = np.random.randint(-5, 6, size=(3, 3, 3))
print(d)
print("-" * 30)

print(LA.det(d))
