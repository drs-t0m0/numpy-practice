import numpy as np

a = np.array([[10, 5, 2, 4, 9, 3, 2], [10, 2, 8, 3, 7, 4, 1]])
print(np.cov(a))
print("-" * 30)

c = np.array([3, 2, 1, 5, 7, 2, 1])
print(np.cov(a, c))
print("#" * 30)

a_transpose = a.T
c_transpose = np.reshape(c, (-1, 1))
print(np.cov(a_transpose, y=c_transpose, rowvar=False))
print("#" * 30)

print(np.cov(a, bias=False))
print("-" * 30)

# Nで割るので値が少しずつ減少する
print(np.cov(a, bias=True))
print("#" * 30)

print(np.cov(a, ddof=None))
print("-" * 30)
print(np.cov(a, ddof=0))
print("-" * 30)
print(np.cov(a, ddof=1))
print("-" * 30)
print(np.cov(a, ddof=2))
print("#" * 30)

print(a)
print("-" * 30)

# 左から２,３番めの生徒の点数を重要視する
fweights = np.array([1, 2, 2, 1, 1, 1, 1])
print(np.cov(a, fweights=fweights))
print("#" * 30)

# 2,3,4番目の生徒の点数を重視する
aweights = np.array([0.1, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1])
print(np.cov(a, aweights=None))
print("-" * 30)
print(np.cov(a, aweights=aweights))
