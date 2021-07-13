import numpy as np

print(np.arange(5))
print("-" * 30)

# 負の値を指定すると要素を持たない配列を返す
print(np.arange(-10))
print("-" * 30)

print(np.arange(4.5))
print("#" * 30)

# 等差を指定しないので等差は1
print(np.arange(1, 8))
print("-" * 30)
print(np.arange(2, 10))
print("-" * 30)
print(np.arange(0.5, 5.5))
print("-" * 30)
print(np.arange(0.55, 5.55))
print("#" * 30)

# 等差を指定
print(np.arange(2, 12, 2))
print("-" * 30)
print(np.arange(2, 5, 0.2))
print("-" * 30)
print(np.arange(5, 2, -1))
print("#" * 30)

# データ型を指定
print(np.arange(5, dtype='float64'))
print("-" * 30)
print(np.arange(5.0, dtype='int'))
print("-" * 30)
print(np.arange(0, 5, 0.5, dtype='int'))
print("-" * 30)
print(np.arange(0, 5, 1.5, dtype='int'))
print("-" * 30)
