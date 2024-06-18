N = int(input())
h = list(map(int,input().split()))
num = 0
ans = h[-1]

for i in range(N):
  ans += abs(h[i] - num)
  num = h[i]
  
print(ans // 2)