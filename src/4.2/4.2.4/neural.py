import numpy as np
import pandas as pd

df = pd.read_csv('iris.data', header=None)
print(df)

# 中身を見ると最初の100個分のデータがIris setonaとIris virginicaのものとなっているのでそこのラベルデータだけ抜き出す
y = df.iloc[0:100, 4].values
# ラベルがIris setonaなら-1、Iris virginicaだったら1として数値変換する
y = np.where(y == 'Iris-setona', -1, 1)
# 1~4番目のデータが今回学習に使うものなのでそれを抜き取る
X = df.iloc[0:100, [0, 1, 2, 3]].values

# データを入れるための空の配列を作る
X_train = np.empty((80, 4))
X_test = np.empty((20, 4))
y_train = np.empty(80)
y_test = np.empty(20)

X_train[:40], X_train[40:] = X[:40], X[50:90]
X_test[:10], X_test[10:] = X[40:50], X[90:100]
y_train[:40], y_train[40:] = y[:40], y[50:90]
y_test[:10], y_test[10:] = y[40:50], y[90:100]

print("#" * 30)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def activation(X, w, b):
    return sigmoid(np.dot(X, w) + b)


def loss(X, y, w, b):
    dif = y - activation(X, w, b)
    return np.sum(dif ** 2 / (2 * len(y)), keepdims=True)


def predict(X, w, b):
    result = np.where(activation(X, w, b) < 0.5, -1.0, 1.0)
    return result


def accuracy(X, y, w, b):
    pre = predict(X, w, b)
    return np.sum(np.where(pre == y, 1, 0)) / len(y)


# 解析的に重みの更新を行う。etaは学習率
def update(X, y, w, b, eta):
    a = (activation(X, w, b) - y) * activation(X, w, b) * (1 - activation(X, w, b))
    a = a.reshape(-1, 1)
    w -= eta * 1 / float(len(y)) * np.sum(a * X, axis=0)
    b -= eta * 1 / float(len(y)) * np.sum(a)
    return w, b


# w,bの値をそれぞれ少しだけ増加させたときにどれほど値が変動するかを計算することで偏微分を計算する
def update_2(X, y, w, b, eta):
    h = 1e-4
    loss_origin = loss(X, y, w, b)
    delta_w = np.zeros_like(w)
    delta_b = np.zeros_like(b)
    for i in range(4):
        tmp = w[i]
        w[i] += h  # パラメーターのうちの１つの値だけ少しだけ増加させる
        loss_after = loss(X, y, w, b)
        delta_w[i] = eta * (loss_after - loss_origin) / h
        w[i] = tmp
    tmp = b
    b += h
    loss_after = loss(X, y, w, b)
    delta_b = eta * (loss_after - loss_origin) / h
    w -= delta_w  # 値の更新
    b = tmp - delta_b
    return w, b


# wの初期値は全部0.1
weights_1 = np.ones(4) / 10
# bも初期値を0.1にする
bias_1 = np.ones(1) / 10

weights_2 = np.ones(4) / 10
bias_2 = np.ones(1) / 10

# とりあえず15回ほど学習させてみる
for _ in range(15):
    weights_1, bias_1 = update(X_train, y_train, weights_1, bias_1, eta=0.1)
    weights_2, bias_2 = update(X_train, y_train, weights_2, bias_2, eta=0.1)
    print('acc_1  %f, loss_1 %f, acc_2 %f, loss_2 %f' % (accuracy(X_test, y_test, weights_1, bias_1),
                                                         loss(X_train, y_train, weights_1, bias_1),
                                                         accuracy(X_test, y_test, weights_2, bias_2),
                                                         loss(X_test, y_test, weights_2, bias_2)))

print('weights_1 = ', weights_1, 'bias_1 = ', bias_1)
print('weights_2 = ', weights_2, 'bias_2 = ', bias_2)
