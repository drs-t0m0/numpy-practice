import numpy as np

print(np.eye(3))
print("-" * 30)
print(np.eye(10))
print("#" * 30)

print(np.eye(2, 3))
print("-" * 30)
print(np.eye(5, 4))
print("#" * 30)

print(np.eye(5, k=0))
print("-" * 30)

# 上方に１つ移動
print(np.eye(5, k=1))
print("-" * 30)

# 下方に１つ移動
print(np.eye(5, k=-1))
print("-" * 30)

print(np.eye(5, k=3))
print("#" * 30)

print(np.eye(5, dtype=int))
print("-" * 30)
print(np.eye(5, dtype=complex))
