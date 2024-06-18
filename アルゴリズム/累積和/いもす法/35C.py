# 累積和 いもす法
N, Q = map(int,input().split())
A = [0]*(N + 1)  # Aの一番最後のデータは不要なため出力しない
ans = []

for _ in range(Q):
  l, r = map(int,input().split())
  A[l - 1] += 1
  A[r] -= 1

for i in range(1,N + 1):
  A[i] += A[i - 1]

for i in range(N):
  if A[i] % 2 == 0:
    ans.append('0')
  else:
    ans.append('1')

print(''.join(ans))