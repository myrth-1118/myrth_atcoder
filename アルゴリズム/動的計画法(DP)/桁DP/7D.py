# 桁DP
a, b = map(int,input().split())

def keta_dp(s):
  A = []
  for i in str(s):   # sを一桁ごとに分解
    A.append(int(i))
  n = len(A)
  dp = [[[0]*2 for _ in range(2)] for _ in range(n + 1)]
  dp[0][0][0] = 1  # 初期値の設定

  for i, x in enumerate(A):    # i=何桁目 x=数字
    for j in range(2):         # 0→False 1→True  0には4と9を含まない個数、1には4と9を含む個数が入る
                               # j 0→0or1に遷移する 1→1のみに遷移する 
      for k in range(2):       # k jと挙動は同じ kでsとの大小関係を決める 0→不明 1→sより小さい確定 
      
        if k == 0:                # k=0のときは(0~x) k=1のときは既に確定しているから全部(0~9)
          for d in range(x + 1):  # i桁目がsと同じになるまで
            dp[i + 1][j or d == 4 or d == 9][k or d < x] += dp[i][j][k]
        else:
          for d in range(10):
            # 左辺→ [j]は d=4,9 のときTrueとなり[1]となる　
            # 左辺→ [k]はd<xのときTrueで[1]、d=xのときFalseで[0]になる k=1のときはdに関係なくTrueで[1]
            dp[i + 1][j or d == 4 or d == 9][k or d < x] += dp[i][j][k]
  
  return dp[n][1][0] + dp[n][1][1] # 4と9を含む数字の個数は j=1 に入っている
  
a_num = keta_dp(a - 1)
b_num = keta_dp(b)

print(b_num - a_num)