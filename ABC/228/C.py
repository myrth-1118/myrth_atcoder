N, K = map(int,input().split())
P = []                  # i番目の合計点を記録

for i in range(N):
  Pi = list(map(int,input().split()))
  P_sum = sum(Pi)
  P.append(P_sum)

A = sorted(P,reverse=True)

for i in range(N):
  if P[i] >= A[K - 1] - 300:
    print('Yes')
  else:
    print('No')