# 配列同士を連結する、NumPyのvstackとhstack関数の使い方

ndarrayは、Pythonのリストとは違い、+などの演算子で結合することができない

## hstack

2次元でいうと、水平方向に(horizontal)連結する  
厳密にいうと、axis=1の方向に結合される  
結合後は、先頭を0番目としてshapeの1番目の要素数が増える

## vstack

2次元でいうと縦方向(vertical)に連結する  
厳密にいうと、axis=0の方向に結合される  
