H, W = map(int,input().split())
S = [input() for i in range(H)]
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]

for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      flag = False
      for k in range(4):
        if 0 <= i + y[k] < H and 0 <= j + x[k] < W:
          if S[i + y[k]][j + x[k]] == '#':
            flag = True
            
      if flag == False:
        print('No')
        exit()

print('Yes')