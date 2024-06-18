N = int(input())
A = list(map(int,input().split()))
node = [0]*(N + 1)

node[0] = abs(A[0])
node[-1] = abs(A[-1])

money = abs(A[0]) + abs(A[-1])

for i in range(N - 1):
  node[i + 1] = abs(A[i] - A[i + 1])
  money += node[i + 1]

for i in range(N):
  if i == 0:
    print(money - node[0] - node[1] + abs(A[1]))
  elif i == N - 1:
    print(money - node[-1] - node[-2] + abs(A[-2]))
  else:
    print(money - node[i] - node[i + 1] + abs(A[i - 1] - A[i + 1]))