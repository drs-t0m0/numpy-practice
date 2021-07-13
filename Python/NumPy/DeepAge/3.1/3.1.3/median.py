import numpy as np

a = np.random.randint(100, size=(2, 3, 4))
print(a)
print("-" * 30)
print(np.median(a))
print("#" * 30)

# axis=2の軸方向に沿った中央値を求めていく
print(np.median(a, axis=2))
print("-" * 30)

# axis=1の軸方向に沿った中央値を求めていく
print(np.median(a, axis=1))
print("-" * 30)

# 2つ指定すると２次元の中での中央値を出してくれる
print(np.median(a, axis=(1, 2)))
print("#" * 30)

b = a.copy()
print(b)
print("-" * 30)

print(np.median(b, axis=1, overwrite_input=True))
print("-" * 30)

print(np.all(a == b))
print("-" * 30)

print(a)
print("-" * 30)
print(b)
print("#" * 30)

print(np.median(a, axis=0, keepdims=True))
print("-" * 30)
print(np.median(a, axis=1, keepdims=False))
print("-" * 30)
print(np.median(a, axis=1, keepdims=True))
print("-" * 30)
print(np.median(a, axis=(0, 2), keepdims=True))
