N = int(input())
x = []
y = []
H = []
for i in range(N):
  xi, yi, Hi = map(int,input().split())
  x.append(xi)
  y.append(yi)
  H.append(Hi)
  
for i in range(N):  # 中心の基準とする値の設定
  if H[i] != 0:    
    x0 = x[i]
    y0 = y[i]
    H0 = H[i]
  
for i in range(101):
  for j in range(101):
    flag = True
    C = abs(i - x0) + abs(j - y0) + H0        # 中心が(i,j)の場合の高さ
 
    for k in range(N):
      if H[k] == 0:                           # 高さ0のときは他と異なる
        if abs(i - x[k]) + abs(j - y[k]) < C:
          flag = False
          
      else:
        if abs(i - x[k]) + abs(j - y[k]) + H[k] != C:
          flag = False
    
    if flag == True:
      print(i,j,C)
      exit()