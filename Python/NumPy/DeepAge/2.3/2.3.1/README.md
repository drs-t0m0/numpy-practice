# np.loadtxtとnp.savetxtでテキストファイルを読み書きする方法

ndarrayの永続化方法としてsave、load関数がある  
aveやloadを使うと、pickleやnpy、npz形式のファイルに読み書きすることでndarrayと変換することができる

しかし一方で、他のプログラミング言語やツールなどからデータを読み込むことができなくなる np.loadtextとnp.savetxt関数を使用することで、このような問題を解決しながらNumPyとデータ互換を維持する

## np.load、np.save関数の特徴

- 配列をそのまま保存できる、3次元以上の配列も保存可能
- 対応拡張子はpickle、npz、npy
- ただし、扱うファイル形式は他のアプリケーションなどとの互換性はほとんどない

## np.loadtxt、np.savetxt関数の特徴

- 他のアプリケーションと互換性のある.dat、.csv、.txt形式のファイルの読み書きができる
- 保存できる配列の次元は二次元まで

## np.genfromtxt

np.genfromtxtを使うことで、データの欠落に対する挙動を指定することができる
