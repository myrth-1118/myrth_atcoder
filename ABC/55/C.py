N, M = map(int,input().split())

if 2*N >= M:
  print(M // 2)
else:
  print(N + ((M - N*2) // 4))