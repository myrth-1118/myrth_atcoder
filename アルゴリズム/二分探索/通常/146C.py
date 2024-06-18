# 二分探索
A, B, X = map(int,input().split())

def check(n):
  S = str(n)
  if A*n + B*len(S) <= X:
    return True
  else:
    return False

l = 0
r = 10**9 + 1

while r - l > 1:
  m = (r + l) // 2
  if check(m):
    l = m
  else:
    r = m

print(l)