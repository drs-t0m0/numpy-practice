import numpy as np

a = np.random.randn(1000)
print(np.histogram(a))
print("-" * 30)

# こうすればヒストグラムをビンの境界の値を2つの変数に格納できる
hist, bins = np.histogram(a)
print(hist)
print("-" * 30)
print(bins)
print("#" * 30)

c = np.random.randint(10, size=30)
print(c)

print(np.histogram(c, range=(0, 10)))
print("-" * 30)
print(np.histogram(c))
print("-" * 30)

d = np.random.randn(40)
print(d)
print("-" * 30)

print(np.histogram(d, range=(-3, 3)))
print("#" * 30)

# ビンの数を減らしたいときはbinsに数値を指定すればよい
print(np.histogram(a, bins=5))
print("-" * 30)

print(np.histogram(a, bins=np.arange(-3, 3)))
print("-" * 30)

print(np.histogram(a, bins=np.linspace(-3, 3, 20)))
print("#" * 30)

b = np.random.randint(-3, 4, size=20)
print(b)
print("-" * 30)

weights = np.tile(np.array([1, 0]), 10)
print(weights)
print("-" * 30)

# 重みを設定してヒストグラムを求めて見る
print(np.histogram(b, bins=6, weights=weights))
print("#" * 30)

print(b)
print("-" * 30)

# まずはFalseで見て見る
print(np.histogram(b, bins=6, density=False))
print("-" * 30)

# まずはTrueだと標準化されて値が1/20される（度数の合計が20で、ビンの幅がそれぞれ1なので)
print(np.histogram(b, bins=6, density=True))
