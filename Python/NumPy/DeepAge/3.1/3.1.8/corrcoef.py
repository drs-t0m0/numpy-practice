import numpy as np

x = np.array([
    [1, 2, 1, 9, 10, 3, 2, 6, 7],
    [2, 1, 8, 3, 7, 5, 10, 7, 2]
])

# 相関関数行列を求める
# 右上と左下の値が相関係数となっている
print(np.corrcoef(x))
print("#" * 30)

y = np.array([2, 1, 1, 8, 9, 4, 3, 5, 7])
print(np.corrcoef(x, y))
print("-" * 30)

x_transpose = x.T

# rowvar=Falseにすることで列ごとに相関係数を求める
print(np.corrcoef(x_transpose, rowvar=False))
print("-" * 30)

# rowvar=True(デフォルト)のままにすると生徒ごとの相関係数を求めることになる
print(np.corrcoef(x_transpose, rowvar=True))
print("-" * 30)
