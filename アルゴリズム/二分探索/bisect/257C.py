# 二分探索bisect  
import bisect
N = int(input())
S = input()
W = list(map(int,input().split()))
a, c = [], []

for i in range(N):
  if S[i] == '1':
    a.append(W[i])
  else:
    c.append(W[i])
    
a.sort()
c.sort()
W.sort()
ans = len(a)

for i in W:
  a_num = len(a) - bisect.bisect_right(a,i)
  c_num = bisect.bisect_right(c,i)
  ans = max(ans, a_num + c_num)

print(ans)