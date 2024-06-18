N = int(input())
X = list(map(int,input().split()))
ans = 10**10

for i in range(101):
  num = 0
  for j in X:
    num += (i - j)**2
    
  ans = min(ans,num)

print(ans)