N, M = map(int,input().split())
H = list(map(int,input().split()))
node = [True]*N

for i in range(M):
  A, B = map(int,input().split())
  if H[A - 1] == H[B - 1]:
    node[A - 1] = False
    node[B - 1] = False
    
  elif H[A - 1] > H[B - 1]:
    node[B - 1] = False
    
  else:
    node[A - 1] = False
  
print(sum(node))  # Trueの合計を数える