from collections import defaultdict
N, M = map(int,input().split())
S = input()
C = list(map(int,input().split()))
num = defaultdict(list)
node = [0]*N

for i in range(N):
  num[C[i]].append((S[i],i))

for i in num:
  for j in range(len(num[i])):
    node[num[i][j][1]] = num[i][j - 1][0]
    
print(''.join(node))