N = int(input())
S = input()
a = [[0,0]]
nx, ny = 0, 0      # 現在地
x = [1,-1,0,0]
y = [0,0,1,-1]

for i in range(len(S)):
  if S[i] == 'R':
    nx += x[0]
    ny += y[0]
  if S[i] == 'L':
    nx += x[1]
    ny += y[1]
  if S[i] == 'U':
    nx += x[2]
    ny += y[2]
  if S[i] == 'D':
    nx += x[3]
    ny += y[3]
    
  a.append([nx, ny])

a = list(map(list,set(map(tuple,a))))    # ２次元配列の重複を削除

if len(a) == N + 1:
  print('No')
else:
  print('Yes')