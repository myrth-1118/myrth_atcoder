# 繰り返し2乗法
# 逆元
N = int(input())
MOD = 998244353
k = len(str(N))

# (10**k)**n - 1 / 10**k - 1 をMODで割ったあまりを求めればいい
# それぞれMODで割る → a / b → bの逆元を考える

def mod_exp(base,exp,mod): #base=n乗するもの, exp=n乗
  result = 1         # 初期値
  while exp > 0:
    if exp % 2 == 1: # expが奇数のとき
      result = (result*base) % mod
    base = (base*base) % mod
    exp //= 2
  return result

a = (mod_exp(10, k*N, MOD) - 1) % MOD
b = (mod_exp(10, k, MOD) - 1) % MOD

c = pow(b, MOD - 2, MOD)  # bの逆元

print(N*a*c % MOD)