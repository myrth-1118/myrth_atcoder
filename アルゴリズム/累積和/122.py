# 累積和
N, Q = map(int,input().split())
S = input()
check = [0]*N

for i in range(N - 1):
  check[i + 1] = check[i]
  if S[i] == 'A' and S[i + 1] == 'C':
    check[i + 1] += 1

for i in range(Q):
  l, r = map(int,input().split())
  print(check[r - 1] - check[l - 1])