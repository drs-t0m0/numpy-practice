import numpy as np

# 何も値を設定しないと１つだけ値を返す
print(np.random.rand())
print("-" * 30)

# 0~9の範囲にあるのランダムな整数を返す
print(np.random.randint(10))
print("-" * 30)

# 2×3の乱数配列
print(np.random.rand(2, 3))
print("-" * 30)

# size(デフォルトはNone)に配列の形を代入
print(np.random.randint(10, size=(2, 3)))
print("-" * 30)

# 5以上10"未満"の範囲でのランダムな整数を返す
print(np.random.randint(5, 10, size=(2, 3)))
print("-" * 30)

# 5以上10"未満""の範囲でランダムな実数を返す
print((10 - 5) * np.random.rand(10) + 5)
print("#" * 30)

np.random.seed(seed=21)
print(np.random.rand())
print("-" * 30)

np.random.seed(seed=21)
print(np.random.rand())  # 同じ値が返されます。
print("-" * 30)

np.random.seed(seed=10)
print(np.random.rand(20))
print("-" * 30)

np.random.seed(seed=23)
print(np.random.rand(20))
print("-" * 30)

np.random.seed(seed=10)  # 同じ値が返されます。
print(np.random.rand(20))
print("-" * 30)

np.random.seed(seed=23)  # 同じ値が返されます。
print(np.random.rand(20))
