N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
num = 0
ans = 0

for i in range(N):
  if num + B[i] >= A[i]:
    ans += A[i]
    num = B[i] - max(0, A[i] - num)
  
  else:
    ans += num + B[i]
    num = 0

ans += min(A[-1],num)   # N+1番目の街で倒せるモンスターの数

print(ans)