# 順列全探索 順列重複なし
import itertools
N, M = map(int,input().split())
node = [[] for _ in range(N)]
arr = []
ans = 0
for i in range(M):
  a, b = map(int,input().split())
  node[a - 1].append(b)
  node[b - 1].append(a)

for i in range(2, N + 1):
  arr.append(i)

arr_list = list(itertools.permutations(arr))

for ptn in arr_list:
  flag = True
  temp = 1     # 現在地
  
  for i in range(len(ptn)):
    if ptn[i] in node[temp - 1]:   # nodeに次の数字が入っていた場合
      temp = ptn[i]
    else:
      flag = False
  
  if flag:
    ans += 1

print(ans)