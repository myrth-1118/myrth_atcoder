N, M, H, K = map(int,input().split())
S = input()
items = set(tuple(map(int, input().split())) for _ in range(M))
x, y = 0, 0

for i in range(N):
  if S[i] == 'R':
    x += 1
  if S[i] == 'L':
    x -= 1
  if S[i] == 'U':
    y += 1
  if S[i] == 'D':
    y -= 1
  
  H -= 1
  if H == -1:
    print('No')
    exit()
  else:
    if H < K and (x, y) in items:
      H = K
      items.remove((x, y))

print('Yes')