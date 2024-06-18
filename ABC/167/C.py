from itertools import product     # bit全探索
N, M ,X = map(int,input().split())
C = []
A = []

for i in range(N):
  c, *a = map(int,input().split())
  C.append(c)
  A.append(a)
  
ans = sum(C) + 1                   # ansの初期値がsum(C)だとすべて購入したときの成否が判別できない
for pro in product((0,1),repeat=N):
  H = [0]*M
  money = 0
  f = True
  
  for i in range(N):     # かかる金額
    if pro[i] == 1:
      money += C[i]  
      
      for j in range(M): # 得られるスキル
        H[j] += A[i][j]  
      
  for i in range(M):
    if H[i] < X:
      f = False
  
  if f:
    ans = min(ans,money)

if ans == sum(C) + 1:   # すべて購入しても足りない場合
  print(-1)
else:
  print(ans)