from collections import defaultdict
N = int(input())
num_L = defaultdict(lambda: float('-inf'))  # 各点yで左向きの人の最大値を記録
num_R = defaultdict(lambda: float('inf'))   # 各点yで右向きの人の最小値を記録
check = []

for i in range(N):
  x, y = map(int,input().split())
  check.append((x, y))

S = input()

for i in range(N):
  x, y = check[i]
  
  if S[i] == 'R':
    if x - num_L[y] < 0:
      print('Yes')
      exit()
 
    num_R[y] = min(num_R[y],x)
  
  else:
    if num_R[y] - x < 0:
      print('Yes')
      exit()

    num_L[y] = max(num_L[y],x)

print('No')