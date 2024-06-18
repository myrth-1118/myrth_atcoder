# 累積和
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 0

node = [0]*(10**6 + 1)
for i in A:
  node[i] += 1

for i in range(10**6):
  node[i + 1] += node[i] 

for a, b in Counter(A).items():    # a=リストの要素 b=個数
  ans += b*(b - 1) // 2            # 同じ数字が複数個ある際、同じ数字で作る組合せの総数
  for i in range(1, 10**6 // a + 1):
    num = node[min(10**6, (i + 1)*a - 1)] - node[i*a - 1]   # 各数字の対応する倍数の個数
    if i == 1:         
      num -= b  # node[a]にはaの個数(b個)が含まれているからそれを除く
      
    ans += num*b*i
    
print(ans)