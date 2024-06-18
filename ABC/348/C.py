N = int(input())
P = {}

for i in range(N):
  A, C = map(int,input().split())
  if C not in P:
    P[C] = A           # 辞書型で受け取る
  else:
    P[C] = min(P[C],A) # Cが同じときは小さい方を格納　O(N)

print(sorted(P.values())[-1])  # maxよりもsortedの方がOが短い