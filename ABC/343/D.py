from collections import defaultdict
N, T = map(int,input().split())
# 各点数の人数
node = defaultdict(int)
node[0] = N
ans = 1
# N人のそれぞれの点数
score = [0]*(N + 1)

for _ in range(T):
  A, B = map(int,input().split())
  p = score[A]
  node[p] -= 1
  
  if node[p] == 0:
    ans -= 1
  
  score[A] += B
  q = score[A]
  node[q] += 1
  
  if node[q] == 1:
    ans += 1
  
  print(ans)