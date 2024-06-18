# 1次元DP
N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

node = [0]*N
node[0] = T[0]

for i in range(1,N):
  node[i] = min(T[i], node[i - 1] + S[i - 1])

if node[0] > node[N - 1] + S[N - 1]:
  node[0] = node[N - 1] + S[N - 1]
  num = 1
  
  while node[num] > node[num - 1] + S[num - 1]:
    node[num] = node[num - 1] + S[num - 1]
    num += 1

for i in node:
  print(i)