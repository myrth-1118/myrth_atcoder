# 順列全探索 順列重複なし
import itertools  
S, K = map(str,input().split())
arr = []
a = []
for i in range(len(S)):
  arr.append(S[i])

arr_list = list(itertools.permutations(arr))   # Sの各文字を使用した全パターン列挙

A = sorted(set(arr_list))      # 重複をなくして辞書順にソートする
print(''.join(A[int(K) - 1]))