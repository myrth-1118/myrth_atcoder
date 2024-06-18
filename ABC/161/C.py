N, K = map(int,input().split())
a = N // K 
num = N
ans = N

if N >= K:
  num = N - a*K

for i in range(2):
  p = K - num
  ans = min(ans,p)
  num = p

print(ans)