import numpy as np

# -4~4の範囲での一様乱数
x = np.random.rand(20) * 8 - 4
print(x)
print("-" * 30)

y = np.sin(x) + np.random.randn(20) * 0.2
print(y)
print("#" * 30)

# 行列Aの受け皿を作る
a = np.empty((6, 6))

for i in range(6):
    for j in range(6):
        a[i][j] = np.sum(x ** (i + j))

print(a)
print("-" * 30)

b = np.empty(6)

for i in range(6):
    b[i] = np.sum(x ** i * y)

print(b)
print("-" * 30)

# linalg.inv()で逆行列を求める。dot関数で内積を求めてくれる
omega = np.dot(np.linalg.inv(a), b.reshape(-1, 1))
print(omega.shape)
print("-" * 30)

# ωを係数とした多項式を作る
f = np.poly1d(omega.flatten()[::-1])
xx = np.linspace(-4, 4, 100)

print(f(xx))
print("#" * 30)

omega_2 = np.polyfit(x, y, 5)
print(omega_2)

f_2 = np.poly1d(omega_2)
