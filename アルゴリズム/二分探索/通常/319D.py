# 二分探索
N, M = map(int,input().split())
L = list(map(int,input().split()))

def check(x):
  num = 1
  total = L[0]
  
  for i in range(1, N):
    if total + L[i] + 1 <= m:
      total += L[i] + 1
    else:
      num += 1
      total = L[i]
  return num

l = max(L) - 1
r = sum(L) + N - 1

while r - l > 1:
  m = (r + l) // 2
  if check(m) <= M:  # 合計がM行以下だったら幅の右端を小さくする
    r = m
  else:              # 合計がM + 1行以上だったら幅の左端を大きくする
    l = m

print(r)