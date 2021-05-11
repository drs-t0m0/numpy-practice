import numpy as np

print(np.newaxis is None)
print("#" * 30)

x = np.arange(15).reshape(3, 5)
print(x)
print("-" * 30)

# １つ次元を追加してスライシング
print(x[np.newaxis, :, :])
print("-" * 30)

# axis=1のところに入れることも可能
print(x[:, np.newaxis, :])
print("-" * 30)

# Noneで代用も可能
print(x[:, None, :])
print("#" * 30)

x = x.flatten()
print(x)
print("-" * 30)

# xを縦ベクトルに
print(x[:, np.newaxis])
print("-" * 30)
