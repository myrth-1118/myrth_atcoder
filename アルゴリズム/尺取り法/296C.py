# 尺取り法
N, X = map(int,input().split())
A = list(map(int,input().split()))
a = sorted(A)
P = []
flag = False

if X == 0:
  flag = True
else:
  r, num = 0, a[0]       # r=右端  num=左端の値
  for i in range(0,len(a) - 1):     # i=左端
    while r < len(a) and a[r] - num < abs(X): # rが右端に到達or差が大きいとき
      r += 1
      
    if r < len(a) and a[r] - num == abs(X):
      flag = True
      break
    elif i == r:      # 左端と右端が同じとき
      r += 1
    else:
      num = a[i + 1]

if flag:
  print('Yes')
else:
  print('No')