N = int(input())
B = list(map(int,input().split()))
ans = B[0] + B[-1]

for i in range(N - 2):
  if B[i] <= B[i + 1]:
    ans += B[i]
  else:
    ans += B[i + 1]

print(ans)