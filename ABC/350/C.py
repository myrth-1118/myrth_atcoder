N = int(input())
A = list(map(int,input().split()))
node = []
ans = []

for i in range(N):
  node.append([A[i], i + 1])

node.sort()

for i in range(N - 1):
  if node[i][0] != node[i][1]:
    ans.append((i + 1, node[i][1]))  # 変化させるindex
    
    num = A[node[i][0] - 1]
    node[num - 1][1] = node[i][1]
    node[i][1] = i + 1
    A[node[num - 1][1] - 1] = num
    A[i] = i + 1 
    
print(len(ans))
for i in ans:
  print(*i)