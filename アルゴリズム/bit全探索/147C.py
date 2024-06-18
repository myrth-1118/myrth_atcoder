# bit全探索
from itertools import product
N = int(input())
L = [[] for i in range(N)]
ans = 0

for i in range(N):
  A = int(input())
  for _ in range(A):
    x, y = map(int,input().split())
    L[i].append([x, y])

for pro in product((0,1),repeat=N):   # 0と1から成る長さNの組み合わせの全列挙
  Flag = True
  num = 0
  for i in range(N): 
    if pro[i] == 1:
      num += 1
      
  for j in range(N):
    for x,y in L[j]:        # この受け取り方だとx,yの座標を指定しなくてよい
      if pro[j] == 1:       # 正直者の場合
        if pro[x - 1] != y:
          Flag = False
  if Flag:                  # 不親切の場合は真偽不明だから考慮しない
    ans = max(ans,num)

print(ans)