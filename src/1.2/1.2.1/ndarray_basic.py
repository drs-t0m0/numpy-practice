import numpy as np
import time

# T,data,dtype: 属性がどのように表示されるのか
a = np.array([1, 2, 3])

# クラスを確認
print(type(a))
print("-" * 30)

b = np.array([[1, 2, 3], [4, 5, 6]])
# 転置
print(b)
print("-" * 30)
print(b.T)
print("-" * 30)

# メモリの位置
print(a.data)
print("-" * 30)

# データ型
print(a.dtype)
print("#" * 30)

# flags,flat: メモリレイアウトについての情報
print(a.flags)
print("-" * 30)
print(b.flags)
print("-" * 30)

# 1次元配列へと変換
print(a.flat[1])
print("-" * 30)
print(b.flat[4])
print("#" * 30)

# real,imag: 複素数(complex)の要素
c = np.array([1. - 2.6j, 2.1 + 3.J, 4. - 3.2j])

# 実部
print(c.real)
print("-" * 30)

# 虚部
print(c.imag)
print("#" * 30)

# size: 要素の数
# itemsize: メモリで占める容量
# nbytes: 配列の要素全ての容量(積)
print(a.size)
print("-" * 30)
print(b.size)
print("-" * 30)
print(a.itemsize)
print("-" * 30)
print(b.itemsize)
print("-" * 30)
print((c.size, c.itemsize))
print("-" * 30)
print(a.nbytes)
print("-" * 30)
print(b.nbytes)
print("-" * 30)
print(c.nbytes)
print("-" * 30)
print(a.size * a.itemsize == a.nbytes)
print("#" * 30)

# ndim,shape: 次元数や形状(shape)について表示
print(a.ndim)
print("-" * 30)
print(b.ndim)
print("-" * 30)
print(a.shape)
print("-" * 30)
print(b.shape)
print("#" * 30)

# strides: 各次元方向に１つ要素を移動するためにはメモリ場で何バイト動く必要があるのかを示す
d = np.array([[[2, 3, 2], [2, 2, 2]], [[4, 3, 2], [5, 7, 1]]])

print((d.shape, d.ndim))
print("-" * 30)
print(a.strides)
print("-" * 30)
print(b.strides)
print("-" * 30)
print(c.strides)
print("-" * 30)
print(d.strides)
print("#" * 30)

# ctypes: ctypesモジュールのイテレータ
# base: ビューをしている元の配列
print(a.ctypes.data)
print("-" * 30)
print(a.base)
print("-" * 30)
e = a[:2]
print(e.base)
print("-" * 30)
print(e.base is a)
print("-" * 30)
print(a.base is e)
print("#" * 30)

# Memory Layout: 内部メモリーでどのように配列が保存されているか
# ローメジャー(row-major)オーダー(=C_CONTIGUOUS): C言語で使われている並べ方: 行方向から順に要素を格納
# カラムメジャー(column-major)オーダー(=F_CONTIGUOUS): フォートランやMatlabで使われている並べ方: 列方向から順に要素を格納
a = np.random.randn(100, 100)
b = np.array(a, order='C')
v = np.array(a, order='F')

print((b.strides, c.strides))
print("-" * 30)

x = np.ones((100000,))
y = np.ones((100000 * 100,))[::100]
print(x.strides)
print("-" * 30)
print(y.strides)
print("-" * 30)
print((x.shape, y.shape))
print("-" * 30)
start_time = time.time()
x.sum()
print(time.time() - start_time)
print("-" * 30)
start_time = time.time()
y.sum()
print(time.time() - start_time)
print("#" * 30)

y_copy = np.copy(np.ones((100000 * 100,))[::100])
print(y_copy.strides)
print("-" * 30)
start_time = time.time()
y_copy.sum()
print(time.time() - start_time)
print("#" * 30)

# ブロードキャスト
a = np.array([1, 2, 3])
b = np.array([[1, 1, 1], [2, 4, 1]])

print(b + a)