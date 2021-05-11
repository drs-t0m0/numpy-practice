import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.r_[a, b])
print("-" * 30)

print(np.r_[2, 5, 3, np.array([2, 3, ]), 4.2])
print("-" * 30)

c = np.zeros((2, 3))
d = np.ones((3, 3))

print(np.r_[c, d])
print("#" * 30)

print(np.r_[0:10])
print("-" * 30)

print(np.r_[:10])
print("-" * 30)

print(np.r_[-10:])
print("-" * 30)

print(np.r_[0:10:2])
print("-" * 30)

print(np.r_[10:0:-1])
print("-" * 30)

print(np.r_[0:10:10j])
print("-" * 30)

print(np.r_[0:9:20j])
print("-" * 30)

print(np.r_[0:10, 0, 4, np.array([3, 3])])
print("#" * 30)

a = np.ones((2, 2))
b = np.zeros((2, 2))

# axis=1(列)方向に結合
print(np.r_['1', a, b])
print("-" * 30)

print(np.r_['1', a, b].shape)
print("-" * 30)

# 今度は行方向に
print(np.r_['0', a, b])
print("-" * 30)

print(np.r_['0', a, b].shape)
print("-" * 30)

# aを指定しない場合はa=0となっている
print(np.r_[a, b].shape)
print("#" * 30)

c = np.ones((2, 2, 2))
d = np.zeros((2, 2, 2))

print(c)
print("-" * 30)
print(d)
print("-" * 30)

print(np.r_['0', c, d])
print("-" * 30)
print(np.r_['1', c, d])
print("-" * 30)
print(np.r_['2', c, d])
print("-" * 30)

print(np.r_['0', c, d].shape)
print("-" * 30)
print(np.r_['1', c, d].shape)
print("-" * 30)
print(np.r_['2', c, d].shape)
print("#" * 30)

# 2次元配列でaxis=0の方向に結合
print(np.r_['0,2', [0, 1, 2], [3, 3, 3]])
print("-" * 30)
print(np.r_['0,2', [0, 1, 2], [3, 3, 3]].shape)
print("-" * 30)

# 3次元配列でaxis=0の方向に結合
print(np.r_['0,3', [0, 1, 2], [3, 3, 3]])
print("-" * 30)
print(np.r_['0,3', [0, 1, 2], [3, 3, 3]].shape)
print("-" * 30)

# 4次元でも。今度は最低次元で結合させる
print(np.r_['-1,4', [0, 1, 2], [3, 3, 3]])
print("-" * 30)
print(np.r_['-1,4', [0, 1, 2], [3, 3, 3]].shape)
print("#" * 30)

# (3,)→(1,3) になってから、axis=0方向に結合
print(np.r_['0,2,-1', [0, 1, 2], [3, 3, 3]])
print("-" * 30)
print(np.r_['0,2,-1', [0, 1, 2], [3, 3, 3]].shape)
print("-" * 30)

# (3,)→(3,1)になってから、axis=0の方向に結合
print(np.r_['0,2,0', [0, 1, 2], [3, 3, 3]])
print("-" * 30)
print(np.r_['0,2,0', [0, 1, 2], [3, 3, 3]].shape)
print("-" * 30)

# 3次元でも同様にできる。 (3,)→(3,1,1)。
print(np.r_['0,3,0', [0, 1, 2], [3, 3, 3]])
print("-" * 30)
print(np.r_['0,3,0', [0, 1, 2], [3, 3, 3]].shape)
print("#" * 30)

a = np.array([1, 4, 6])
b = np.array([2, 2, 2])

print(np.r_['r', a, b])
print("-" * 30)

# 縦ベクトルになる
print(np.r_['c', a, b])
print("-" * 30)

c = np.ones((4, 5))
d = np.zeros((2, 5))

print(np.r_['r', c, d])
print("-" * 30)
print(np.r_['c', c, d])
print("#" * 30)

a = np.ones((3, 2))
b = np.zeros((3, 3))
print(a)
print("-" * 30)
print(b)
print("-" * 30)

print(np.c_[a, b])
print("-" * 30)

c = np.zeros(3)
print(c)
print("-" * 30)

print(np.c_[a, c])
print("-" * 30)

print(np.c_[a, c].shape)
print("-" * 30)

# 1次元配列だと2次元配列として結合される
print(np.c_[[1, 2, 3], [4, 5, 6]])
print("-" * 30)

# 数値だけと結合も可能。前半の２つの配列が２次元配列とならないとできないことに注意
print(np.c_[[[1, 2, 3]], [[4, 5, 6]], 2, 3])