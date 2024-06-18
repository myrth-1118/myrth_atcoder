N, A, B = map(int,input().split())
S = input()
S += S
ans = 10**100

for i in range(N):
  num = A*i
  
  for j in range(N // 2):
    if S[i + j] != S[- 1 - N + i - j]:
      num += B
  ans = min(ans, num)

print(ans)