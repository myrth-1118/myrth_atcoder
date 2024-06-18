# 優先度付きキュー
import heapq             # リストの先頭が必ず最小値となる
from collections import defaultdict
Q = int(input())
mx = []                  # 最大値を取得するリスト
mn = []                  # 最小値を取得するリスト
node = defaultdict(int)  # 個数を格納

for _ in range(Q):
  A = list(map(int,input().split()))
  
  if A[0] == 1:
    x = A[1]
    heapq.heappush(mx, -x)    # 最大値を取得するためマイナスをかける
    heapq.heappush(mn, x)
    node[x] += 1
  
  if A[0] == 2:
    x, c = A[1], A[2]
    node[x] -= min(c, node[x])
  
  if A[0] == 3:
    while node[-mx[0]] == 0:  # mxの先頭(最大値)の個数が0のとき取り出す
      heapq.heappop(mx)
    while node[mn[0]] == 0:
      heapq.heappop(mn)       # mnの先頭(最小値)の個数が0のとき取り出す
    
    a, b = -mx[0], mn[0]
    
    print(a - b)