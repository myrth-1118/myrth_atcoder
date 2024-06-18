N = int(input())
F= []     # 美味しさを収納
S = []    # 味を収納
S_max = 0
ans = 0

for i in range(N):
  f, s = map(int,input().split())
  F.append(f)
  S.append(s)
  
  if s > S_max:
    S_max = s
    num = i

for i in range(N):
  if num != i:
    if F[num] != F[i]:
      ans = max(ans, S_max + S[i])
    else:
      ans = max(ans, S_max + S[i] // 2)

print(ans)