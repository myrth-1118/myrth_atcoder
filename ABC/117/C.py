N, M = map(int,input().split())
X = list(map(int,input().split()))
X.sort(reverse=True)
a = 0
node = []

for i in range(M - 1):
  node.append(X[i] - X[i + 1])
  
if  N >= M:
  print(0)
  exit()

node.sort(reverse=True)
  
for i in range(N - 1):
  a += node[i]

print(sum(node) - a)