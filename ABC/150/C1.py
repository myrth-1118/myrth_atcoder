from itertools import permutations  # 順列全探索
N = int(input())
P = tuple(map(int,input().split())) # tuple() 値を()で括る
Q = tuple(map(int,input().split()))

arr = list(range(1,N + 1))
arr_list = list(permutations(arr))

ans = abs(arr_list.index(P) - (arr_list.index(Q)))

print(ans)