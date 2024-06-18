# 順列全探索 順列重複なし
from itertools import permutations
N = int(input())
P = tuple(map(int,input().split())) # tuple() 値を()で括る
Q = tuple(map(int,input().split())) 

arr = list(range(1,N + 1))          # (0,1,2)のようにリストで返す
arr_list = list(permutations(arr))  # 0~N-1までの順列を全パターン列挙

ans = abs(arr_list.index(P) - (arr_list.index(Q)))

print(ans)