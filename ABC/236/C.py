N, M = map(int,input().split())
S = list(input().split())
T = list(input().split())
now = 0

for i in range(N):
  if S[i] == T[now]:
    now += 1
    print('Yes')
  else:
    print('No')