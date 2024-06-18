H, W, N = map(int,input().split())
T = input()
S = [input() for _ in range(H)]
ans = 0

for i in range(1, H - 1):
  for j in range(1, W - 1):
    y, x = i, j
    flag = True
    
    if S[y][x] == '.':
      for k in T:
        if k == 'U':
          y -= 1
        if k == 'D':
          y += 1
        if k == 'R':
          x += 1
        if k == 'L':
          x -= 1
        if S[y][x] == '#':
          flag = False
          break
        
      if flag:
        ans += 1

print(ans)