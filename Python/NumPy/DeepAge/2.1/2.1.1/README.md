# 配列を形状変換するNumPyのreshapeの使い方

NumPyの配列のshapeの形状変換をする関数reshapeと、似たような機能を持つresize

## reshape

reshapeの引数には、第一引数に変換元になるndarray、第二引数に変換後のarrayの形状(shape)を指定

配列のshapeを指定する際に (n, -1) のように-1を指定すると要素数に合わせてn × mの2次元配列となる

## resize

ほとんどreshapeと変更点はありませんが、こちらは引数にorderがない

reshapeは元の配列の要素数と合致しないとエラーを返しますが、resizeはそのような処理でもエラーを返さずに強制的に実行する