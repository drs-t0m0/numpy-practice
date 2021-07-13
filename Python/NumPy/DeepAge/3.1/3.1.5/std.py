import numpy as np

a = np.random.rand(10)
print(a)
print("-" * 30)
print(np.std(a))
print("#" * 30)

b = np.random.rand(2, 3, 4)
print(b)
print("-" * 30)

# axis=0方向に沿って標準偏差を求める
print(np.std(b, axis=0))
print("-" * 30)

# 2つ指定するとこの２つの軸方向に広がる平面内における標準偏差を求めてくれる
print(np.std(b, axis=(0, 1)))
print("-" * 30)

print(np.std(b, axis=(0, 1, 2)))
print("#" * 30)

print(np.std(b, dtype='float16'))
print("-" * 30)

print(np.std(b, dtype='complex'))
print("#" * 30)

c = np.empty((2, 3))
print(np.std(b, axis=2, out=c))
print("-" * 30)
print(c)
print("#" * 30)

print(np.std(b))
print("-" * 30)

# ddof=1にして不偏標準偏差を表示させる
print(np.std(b, ddof=1))
print("#" * 30)

# keepdims=Trueにすると3次元配列が返される
print(np.std(b, keepdims=True))
print("-" * 30)

print(np.std(b, axis=0, keepdims=True))
print("-" * 30)

print(b / np.std(b, axis=0, keepdims=True))
print("-" * 30)

print(b / np.std(b, axis=0, keepdims=False))
