import numpy as np

a = ['Python', 'Ruby', 'Java', 'JavaScript', 'PHP']

# aから３つの要素をランダムに取り出す
print(np.random.choice(a, 3))
print("-" * 30)

# 重複なしで取り出し
print(np.random.choice(a, 5, replace=False))
print("-" * 30)

# pにリストを渡すことで取り出す値の頻度を変える
# pの値の合計は1になること
print(np.random.choice(a, 20, p=[0.8, 0.05, 0.05, 0.05, 0.05]))
print("-" * 30)

# 最初の引数に整数をわたすと、np.arange(5)で生成される
print(np.random.choice(5, 10))