# 優先度付きキュー
import heapq
N, Q = map(int,input().split())

# 呼ばれた人を保存するリスト
mn = []
num = 1
# 受付に行った人を保存するリスト
node = [False]*(N + 1)

for _ in range(Q):
  n, *a = map(int,input().split())
  
  if n == 1:
    heapq.heappush(mn, num)
    num += 1
  
  if n == 2:
    node[a[0]] = True
  
  if n == 3:
    while node[mn[0]] == True:
      heapq.heappop(mn)
    print(mn[0])