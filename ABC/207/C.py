# 二分探索bisect
import bisect
N = int(input())
node = []
check = []
ans = 0

for i in range(N):  # 優先度順 1.終点含まない 2.始点含む 3.終点含む 4.始点含まない
  t, l, r = map(int,input().split())
  l *= 4
  r *= 4
  if t == 1:
    l += 1
    r += 2
  elif t == 2:
    l += 1
  elif t == 3:
    l += 3
    r += 2
  else:
    l += 3
  
  node.append((l,r))
  check.append(l)
  
node.sort()
check.sort()

for i in range(N):
  x = bisect.bisect_right(check,node[i][1])
  ans += x - i - 1

print(ans)