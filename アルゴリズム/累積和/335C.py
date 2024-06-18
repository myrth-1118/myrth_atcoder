# 累積和 動的配列
N, Q = map(int,input().split())
node = [(1, 0)]  # 頭がi回目の移動後にどこにいるのかを累積和で記録
num = 0

for i in range(Q):
  a, q = input().split()
  A = int(a)
  
  if q in ('U', 'D', 'R', 'L'):
    x, y = node[num][0], node[num][1]
    if q == 'U':
      nx, ny = x, y + 1
    if q == 'D':
      nx, ny = x, y - 1
    if q == 'R':
      nx, ny = x + 1, y
    if q == 'L':
      nx, ny = x - 1, y
    
    node.append((nx, ny))
    num += 1
  
  else:
    b = int(q)
    
    if b - 1 >= num:
      x = b - num
      y = 0
    else:
      x = node[num - b + 1][0]
      y = node[num - b + 1][1]
    
    print(x,y)