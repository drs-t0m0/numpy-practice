import numpy as np
import numpy.linalg as LA

a = np.array([[1, 0], [0, 2]])
print(a)
print("-" * 30)

print(LA.eig(a))
print("-" * 30)

b = np.array([[2, 5], [3, -8]])
print(b)
print("-" * 30)

print(LA.eig(b))
print("#" * 30)

c = np.random.randint(-10, 10, size=(3, 3))
w, v = LA.eig(c)
print(w)
print("-" * 30)
print(v)
print("#" * 30)

c = np.random.randint(-10, 10, size=(3, 3, 3))
print(c)
print("-" * 30)

w, v = LA.eig(c)
print(w)
print("-" * 30)
print(v)
print("-" * 30)
