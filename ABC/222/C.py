N, M = map(int,input().split())
hand = [input() for i in range(N*2)]
P = [[i, 0] for i in range(1, N*2 + 1)]

for i in range(M):
  for j in range(N):
    a = P[j*2][0]
    b = P[j*2 + 1][0]
    x = hand[a - 1][i]
    y = hand[b - 1][i]
    
    if x == y:
      continue
    elif x == 'G' and y == 'C':
      P[j*2][1] += 1
    elif x == 'C' and y == 'P':
      P[j*2][1] += 1
    elif x == 'P' and y == 'G':
      P[j*2][1] += 1
    else:
      P[j*2 + 1][1] += 1
  
  P.sort(key=lambda x: x[0])             # 優先度の低い順にソート
  P.sort(key=lambda x: x[1],reverse=True)

for i, _ in P:
  print(i)