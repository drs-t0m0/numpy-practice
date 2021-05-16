import numpy as np

a = np.array([33, 44, 54, 23, 25, 55, 32, 76])
print(np.average(a))
print("-" * 30)

a = a.reshape(2, 4)
print(a)
print("-" * 30)
# aの形状に関わらず、引数にaxisが指定されていなければ１つのスカラー量だけ返される
print(np.average(a))
print("#" * 30)

# 軸(axis)を指定する。2次元配列でaxis=0のときは行方向の平均を求める
print(np.average(a, axis=0))
print("-" * 30)

# axis = 1のときは列方向の平均を求める
print(np.average(a, axis=1))
print("-" * 30)

b = np.random.rand(24).reshape(2, 3, 4)
print(b)
print("-" * 30)
print(np.average(b, axis=0))
print("-" * 30)
print(np.average(b, axis=1))
print("-" * 30)
print(np.average(b, axis=2))
print("#" * 30)

a = a.flatten()
w = np.array([0.1, 0.05, 0.2, 0.0, 0.0, 0.4, 0.2, 0.05])
# 重みつきの平均を求める
print(np.average(a, weights=w))
print("-" * 30)

w2 = np.array([0.2, 0.8])
a = a.reshape(2, 4)
print(np.average(a, axis=0, weights=w2))
print("#" * 30)

# 重みを設定しないと、各々の要素の重みが1.0に設定されるので、重みの合計は要素数と一致する
print(np.average(a, returned="True"))
print("-" * 30)

a = a.flatten()
print(a)
print("-" * 30)
print(w)
print("-" * 30)
print(np.average(a, weights=w, returned="True"))
