N, T = map(int,input().split())
A = list(map(int,input().split()))

bingo_yoko = [0]*N
bingo_tate = [0]*N
bingo_naname1 = 0
bingo_naname2 = 0
ans = -1

for i in range(T):
  a = (A[i] - 1) // N
  b = (A[i] - 1) % N
  bingo_yoko[a] += 1
  bingo_tate[b] += 1
  if a == b:
    bingo_naname1 += 1
  if a + b == N - 1:
    bingo_naname2 += 1
  
  if max(bingo_yoko) == N or max(bingo_tate) == N or bingo_naname1 == N or bingo_naname2 == N:
    ans = i + 1
    break

print(ans)