import numpy as np

a = np.random.rand(20)
print(a)
print("-" * 30)
print(a.max())
print("-" * 30)

a = a.reshape((4, 5))
print(a)
print("-" * 30)
print(a.max())
print("#" * 30)

print(a.max(axis=0))
print("-" * 30)
print(a.max(axis=1))
print("#" * 30)

b = np.random.rand(30).reshape((2, 3, 5))
print(b)
print("-" * 30)

print(b.max(axis=0))
print("-" * 30)
print(b.max(axis=1))
print("-" * 30)
print(b.max(axis=2))
print("#" * 30)

# NaNが含まれている場合は、NaNが最大値として返す
# NaNを最大値として返して欲しくない場合には、nanmaxを使う
b = np.arange(10, dtype=np.float)
b[3] = np.NaN
print(b.max())
print("-" * 30)
print(np.nanmax(b))
