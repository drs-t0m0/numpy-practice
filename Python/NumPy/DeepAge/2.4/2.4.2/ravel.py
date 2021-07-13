import numpy as np

a = np.arange(10).reshape(2, 5)
print(a)
print("-" * 30)

print(a.ravel())
print("-" * 30)
print(np.ravel(a))
print("#" * 30)

# orderを'C'(初期値)にすると、同じ配列が出て来る
print(a.ravel(order='C'))
print("-" * 30)

# orderを'F'にすると、行方向から値が読み取られる
print(a.ravel(order='F'))
print("-" * 30)

# Fortranスタイルで要素を格納していないのでorder='C'と同じ結果になる
print(a.ravel(order='A'))
print("-" * 30)

# こちらも特に配列の`shape`変更などをしていないので、変化なし
print(a.ravel(order='K'))
print("#" * 30)

b = np.arange(10).reshape(2, 5, order='F')
print(b)
print("-" * 30)

# 連番になる
print(b.ravel(order='F'))
print("-" * 30)

print(b.ravel(order='A'))
print("-" * 30)

# order='C'だと、列方向に読み込む
print(b.ravel(order='C'))
print("#" * 30)

c = b.T

# 連番になる
print(c.ravel())
print("-" * 30)

# メモリの順番を読み込む
print(c.ravel(order='K'))
print("-" * 30)

print(c.T.ravel(order='K'))