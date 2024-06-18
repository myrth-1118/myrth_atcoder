# 2次元DP
N = int(input())
A = []
num = 0
node = [[0]*N for i in range(2)]

for i in range(2):
  Ai = list(map(int,input().split()))
  A.append(Ai)

for i in range(N):
  num += A[0][i]
  node[0][i] = num

node[1][0] = A[0][0] + A[1][0]

for i in range(1,N):
  node[1][i] = max(node[1][i - 1],node[0][i]) + A[1][i]

print(node[-1][-1])