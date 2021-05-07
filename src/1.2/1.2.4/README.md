# NumPyの軸(axis)と次元数(ndim)とは何を意味するのか

## ndarrayの次元数(ndim)とは何か

ndimは多次元配列が何次元の構造をしているのかを意味している  
つまり、shapeの要素の数(=len(arr.shape))

## axisについて

axisは名前の通り座標軸  
3×2の行列の場合、軸順は(行方向, 列方向)

axis = 0: 行方向
axis = 1: 列方向

2×3×2の行列の場合、軸順は(奥, 行方向, 列方向)

axis = 0: 奥
axis = 1: 行方向
axis = 2: 列方向
