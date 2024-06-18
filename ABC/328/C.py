# 二分探索bisect
import bisect
N, Q = map(int,input().split())
S = input()
check = []             # 連続した文字列の場所を記録

for i in range(N - 1):
  if S[i] == S[i + 1]:
    check.append(i + 2)
    
for i in range(Q):
  l, r = map(int,input().split())
  
  l_num = bisect.bisect_right(check,l)
  r_num = bisect.bisect_right(check,r)
  
  print(r_num - l_num)