import bisect      # 二分探索bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
C.sort()
ans = 0

for i in range(N):  # Bの順番
  num_A = 0
  num_C = 0
  
  x = bisect.bisect_right(C,B[i])  # Cの中でBより大きい数字の位置
  num_C += len(C)-x
  
  y = bisect.bisect_left(A,B[i])   # Aの中でBより小さい数字の位置
  num_A += y
  
  ans += num_C * num_A

print(ans)