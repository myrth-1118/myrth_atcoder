# 再帰関数
N = int(input())

def f(n):
  if n == 0:
    return ['#']
  sub = f(n - 1)
  L = len(sub)
  node = [['.']*3*L for _ in range(3*L)]
 
  for i in range(3):
    for j in range(3):
      
      if i != 1 or j != 1:
        for k in range(L):
          for l in range(L):
              node[i*L + k][j*L + l] = sub[k][l]
  
  return node

ans = f(N)
for i in ans:
  print(''.join(i))