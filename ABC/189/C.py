import heapq
from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
node = defaultdict(int)
num_index = defaultdict(int) # 最後に出た場所の座標を格納
mx = []  # 最大値を取得するリスト
ans = 0

heapq.heappush(mx, -A[0])
node[A[0]] = 1
num_index[A[0]] = 1

for i in range(1,N):
  num_index[A[i]] = i + 1
  if -mx[0] < A[i]:   # A[i]の方が大きいとき
    node[A[i]] = i + 1
    heapq.heappush(mx, -A[i]) # 最大値の比較をするため-A[i]を入れる
    
  elif -mx[0] > A[i]: # A[i]の方が大きいとき
    while mx != [] and -mx[0] > A[i]:
      ans = max(ans, -mx[0]*(i + 1 - node[-mx[0]]))
      node[-mx[0]] = 0
      heapq.heappop(mx)
    
    if mx == []:      # A[i]が最も小さいとき
      node[A[i]] = 1
      heapq.heappush(mx, -A[i])
      
    elif -mx[0] < A[i]:
      node[A[i]] = num_index[-mx[0]] + 1
      heapq.heappush(mx, -A[i])

for i in node:
  if node[i] != 0:
    ans = max(ans,i*(N + 1 - node[i]))
    
print(ans)