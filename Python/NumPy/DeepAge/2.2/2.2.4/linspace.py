import numpy as np

# 50個の要素が生成
print(np.linspace(0, 1))
print("-" * 30)
print(np.linspace(0, 49))
print("#" * 30)

# 等差
print(np.linspace(0, 2, 3))
print("-" * 30)
print(np.linspace(0, -2, 3))
print("-" * 30)
print(np.linspace(0, 2, num=3))
print("#" * 30)

# 指定した終点を含むかどうか指定
print(np.linspace(0, 2, num=3, endpoint=False))
print("-" * 30)
print(np.linspace(0, 2, num=3, endpoint=True))  # デフォルト
print("#" * 30)

print(np.linspace(0, 1, retstep=True))
print("-" * 30)
print(np.linspace(0, 2, num=3, retstep=True))
print("-" * 30)
print(np.linspace(0, 2, num=3, retstep=False))  # デフォルト
print("#" * 30)

# データ型
print(np.linspace(0, 2, num=3))
print("-" * 30)

a = np.linspace(0, 1, 3)
print(a.dtype)
print("-" * 30)

print(np.linspace(0, 2, num=3, dtype='int'))
print("-" * 30)
print(np.linspace(0, 1, num=4, dtype='float32'))
print("-" * 30)
print(np.linspace(0, 1, num=4, dtype='float64'))

