# flattenよりも高速に配列を一次元化するnumpy.ravel関数の使い方

np.flatten関数と同様に、配列を一次元化することができる関数だが、  
np.ravel関数の方が高速に処理することができる場合がある

## flattenとの違い

ravel関数はflatten関数とは異なり基本的にはデータのコピーを返さず、破壊的な変更になる