# スライド最小値・最大値
from collections import deque
N, K = map(int,input().split())
P = list(map(int,input().split()))
node = [0]*N
ans = 10**10

for i in range(N):
  node[P[i] - 1] = i

def slide_max_index(a, K): # 区間内の最大値
    N = len(a)
    max_idx = [0]*N  # 各区間内の最大値(index)を格納
    deq = deque()    # 順番待ちの数字を格納

    for i in range(0,N):
      while len(deq) > 0 and deq[0] <= i - K:  # 範囲外になったときの処理
        deq.popleft()
      while len(deq) > 0 and a[deq[-1]] < a[i]: # 最大値にならない数字の処理
        deq.pop()
      deq.append(i)
      max_idx[i] = a[deq[0]]  # indexが欲しい場合は deq[0]にする

    return max_idx

def slide_min_index(a, K): # 区間内の最小値
    N = len(a)
    min_idx = [0]*N
    deq = deque()

    for i in range(0,N):
      while len(deq) > 0 and deq[0] <= i - K:
        deq.popleft()
      while len(deq) > 0 and a[deq[-1]] > a[i]:
        deq.pop()
      deq.append(i)
      min_idx[i] = a[deq[0]]

    return min_idx

A = slide_max_index(node,K)
B = slide_min_index(node,K)

for i in range(K - 1,N):      # 0 ~ K - 2番目まではKより小さい範囲内で考えているため除く
  ans = min(ans,A[i] - B[i])

print(ans)