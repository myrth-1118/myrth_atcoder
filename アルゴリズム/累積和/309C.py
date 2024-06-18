# 累積和
# 二分探索bisect
import bisect
from collections import defaultdict
N, K = map(int,input().split())
node = defaultdict(int)
day = []
num = 0

for i in range(N):
  a, b = map(int,input().split())
  num += b
  node[a] += b
  day.append(a)
  
A = sorted(set(day))
medicine = [0]*(len(A) + 1)
medicine[0] = num

for i in range(len(A)): # i+1日目に必要な薬の量をiに記録
  medicine[i + 1] =  medicine[i] - node[A[i]]
  
A.append(0)
A.sort(reverse=True)
  
M = sorted(medicine)
x = bisect.bisect_right(M,K)
ans = A[x - 1]

print(ans + 1)