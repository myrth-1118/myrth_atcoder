# 1次元DP
S = input()
MOD = 10**9 + 7
dp = [0]*8
check = ['h', 'o', 'k', 'u', 'd', 'a', 'i']

for i in range(len(S)):
  if S[i] == 'c':
    dp[0] += 1
    
  else:
    for j in range(7):
      if S[i] == check[j]:
        dp[j + 1] += dp[j]

print(dp[-1] % MOD)