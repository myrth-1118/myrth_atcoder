# bit全探索
import math
from itertools import product
D, G = map(int,input().split())
p = []
c = []
ans = 1000

for i in range(D):
  pi,ci = map(int,input().split())
  p.append(pi)
  c.append(ci)

for pro in product((0,1),repeat=D):
  score = 0
  num = 0
  
  for i in range(D): 
    if pro[i] == 1:                    # コンプリートの場合
      score += c[i] + p[i]*(i + 1)*100
      num += p[i]
  
  if score < G:
    for i in range(D - 1,-1,-1):       # 逆順
      if pro[i] == 0:
        x = math.ceil((G - score)/((i + 1)*100))   # 少数切り上げ
        if x <= p[i] - 1:
          num += x
          score += x*(i + 1)*100
          break
        else:
          num += p[i] - 1
          score += (p[i] - 1)*(i + 1)*100
          
  if score >= G:
    ans = min(ans,num)

print(ans)