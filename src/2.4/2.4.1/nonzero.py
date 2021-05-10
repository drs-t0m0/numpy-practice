import numpy as np

a = np.random.randint(0, 10, size=20)
print(a)
print("-" * 30)

# 非ゼロ要素のインデックスを取得
print(np.nonzero(a))
print("-" * 30)

# この書式でもOK
print(a.nonzero())
print("-" * 30)

# これで非ゼロ要素抜き出した配列を生成できる。
print(a[np.nonzero(a)])
print("-" * 30)

b = np.random.randint(0, 10, size=(4, 5))
print(b)
print("-" * 30)

# 1つめの配列が行方向のインデックス、
# 2つめの配列が列方向のインデックスになっている
print(np.nonzero(b))
print("-" * 30)

print(b.nonzero())
print("-" * 30)

# 非ゼロ要素を抽出
print(b[b.nonzero()])
print("#" * 30)

# np.where(x!=0)で全く同じことができる
a = np.random.randint(0, 10, size=(100, 100))
b = np.ones(shape=(100, 100))
print(np.where(a != 0, a, b))
print("#" * 30)

# np.argwhere(a)はnp.transpose(np.nonzero(a))と同義
a = np.random.randint(0, 10, size=(100, 100))
print(np.nonzero(a))
print("-" * 30)
print(np.where(a != 0))
print("-" * 30)

print(np.argwhere(a != 0))
print("-" * 30)
print(np.transpose(np.nonzero(a)))
