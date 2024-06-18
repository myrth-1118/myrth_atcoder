L, R = map(int,input().split())
MOD = 2019
ans = 2018

if L // MOD != R // MOD or L % MOD == 0 or R % MOD == 0:
  print(0)
  exit()

else:
  for i in range(L % MOD, R % MOD):
    for j in range(i + 1, R % MOD + 1):
      ans = min(ans, i*j % MOD)

print(ans)