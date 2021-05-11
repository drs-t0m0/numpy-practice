import numpy as np

x = np.arange(15).reshape(3, 5)
print(np.reshape(x, (1, 3, 5)))
print("-" * 30)

print(np.reshape(x, (3, 1, 5)))
print("#" * 30)

# 1次元配列に
x = x.flatten()
print(np.reshape(x, (-1, 1)))