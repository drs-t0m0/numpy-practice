import numpy as np

print(np.genfromtxt('bar.txt', delimiter=','))
print("#" * 30)

print(np.genfromtxt('bar.txt', delimiter=',', dtype=('int', 'float', 'int')))
