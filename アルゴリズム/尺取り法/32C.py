# 尺取り法
N, K = map(int,input().split())
s = [int(input()) for i in range(N)]

if 0 in s:  # 0がある場合は積は0
  print(N)
else:
  r, ans, num = 0, 0, 1  # r=右端 ans=条件を満たすときの数の合計 num=積の合計
  for i in range(N):     # i=左端
    while r < N and num*s[r] <= K: # rが右端に到達or積が大きいとき
      
      num *= s[r]
      r += 1
    ans = max(ans,r - i) # 個数の最大
    
    if i == r:      # 左端と右端が同じとき(s[r]がK以上のとき飛ばす)
      r += 1
    else:
      num //= s[i]  # 積の合計から左端を除く
      
  
  print(ans)