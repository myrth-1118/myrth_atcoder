N, K, Q = map(int,input().split())
P = [0]*N
for i in range(Q):
  A = int(input())
  P[A - 1] += 1

for i in range(N):
  if K - Q + P[i] > 0:
    print('Yes')
  else:
    print('No')