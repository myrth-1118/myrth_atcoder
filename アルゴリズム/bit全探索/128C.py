# bit全探索
from itertools import product
N, M = map(int,input().split())
k = []
s = []
for i in range(M):
  ki, *si = map(int,input().split())
  k.append(ki)
  s.append(si)
  
p = list(map(int,input().split()))
arr = []
ans = 0

for pro in product((0,1),repeat=N):  
  arr.clear()
  flag = True
  for i in range(N):       # onのスイッチをarrに記録
    if pro[i] == 1:
      arr.append(i + 1)

  for i in range(M):
    num = 0
    for j in range(k[i]):
      if s[i][j] in arr:   # onのスイッチの数の確認
        num += 1
    if num % 2 != p[i]:
      flag = False
  if flag == True:
    ans += 1

print(ans)