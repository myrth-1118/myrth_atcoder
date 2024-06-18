# 順列全探索 順列重複なし
import itertools
N, K = map(int,input().split())
T = [list(map(int,input().split())) for i in range(N)]
ans = 0

arr_list = itertools.permutations(range(2,N + 1),N - 1)

for ptn in arr_list:
  num = 0
  now = 1
  for i in ptn:
    num += T[now - 1][i - 1]
    now = i
  
  num += T[now - 1][0]  # 最後に都市1に戻るための時間
  
  if num == K:
    ans += 1

print(ans)