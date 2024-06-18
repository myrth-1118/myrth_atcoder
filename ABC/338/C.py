N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
time = 10**6
ans = 0

for i in range(N):
  if A[i] != 0:
    time = min(time, Q[i] // A[i])

for i in range(time + 1):
  num = 10**6
  for j in range(N):
    if B[j] != 0:
      num = min(num, (Q[j] - A[j]*i) // B[j])
  
  ans = max(ans, i + num)

print(ans)