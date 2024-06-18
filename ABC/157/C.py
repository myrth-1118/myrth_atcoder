N, M = map(int,input().split())
S = []
C = []

for i in range(M):
  s, c = map(int,input().split())
  S.append(s)
  C.append(c)

if N == 1:
  K = 0
else:
  K = 10**(N - 1)

for i in range(K,10**N): # N=1のときは0開始
  a = str(i)
  flag = True
  
  for j in range(M):
    if len(a) < max(S) or int(a[S[j] - 1]) != C[j]:
      flag = False
  
  if flag == True:
    print(i)
    exit()

print(-1)