# 幅優先探索 グラフと頂点
from collections import deque
N = int(input())
node = [[] for _ in range(N)] 
check = [False]*N
time = []

for i in range(N):
  T, K, *A = list(map(int,input().split()))
  time.append(T)
  node[i] = A

q = deque([N - 1])
ans = 0

while len(q) != 0:
  now = q[0]
  q.popleft()
  
  if check[now] == False:
    check[now] = True
    ans += time[now]
    
    for i in node[now]:
      if not check[i - 1]:   # qに追加するのは1つずつ
        q.append(i - 1)
  
print(ans)