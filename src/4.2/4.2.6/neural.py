import numpy as np
import neuralnet as nl
import load_mnist

dataset = load_mnist.load_mnist()
X_train = dataset['x_train']
t_train = dataset['t_train']
X_test = dataset['x_test']
t_test = dataset['t_test']

weight_list, bias_list = nl.make_params([784, 100, 10])
# 何回学習を行うか指定します
train_time = 10000
# 1回の学習でいくつのデータを学習するかを指定します。
batch_size = 1000
# 精度と損失がどれだけ変動したかを記録する配列を作る
total_acc_list = []
total_loss_list = []

for i in range(train_time):
    # 0~59999でランダムな整数をbatch_size分だけ発生させる
    ra = np.random.randint(60000, size=batch_size)
    x_batch, t_batch = X_train[ra, :], t_train[ra, :]
    weight_list, bias_list = nl.update(x_batch, weight_list, bias_list, t_batch, eta=2.0)
    # ここでパラメータの更新をおこなう。etaは学習率でどれぐらいの割合でパラメータを更新するかを決める
    # 今回は2.0で行う
    # 実際は試行錯誤してこの値を決めていくことになる
    # ５回ごとにどれぐらい学習できているかを確かめる
    if (i + 1) % 100 == 0:
        acc_list = []
        loss_list = []
        for k in range(10000 // batch_size):
            x_batch, t_batch = X_test[k * batch_size:(k + 1) * batch_size, :], \
                               t_test[k * batch_size:(k + 1) * batch_size, :]
            acc_val = nl.accuracy(x_batch, weight_list, bias_list, t_batch)
            loss_val = nl.loss(x_batch, weight_list, bias_list, t_batch)
            acc_list.append(acc_val)
            loss_list.append(loss_val)
        acc = np.mean(acc_list)
        loss = np.mean(loss_list)
        total_acc_list.append(acc)
        total_loss_list.append(loss)
        print("Time; %d, Accuracy: %f, Loss: %f" % (i + 1, acc, loss))
