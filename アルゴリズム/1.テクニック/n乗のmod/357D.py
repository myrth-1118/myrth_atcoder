# 繰り返し2乗法
# 逆元
N = int(input())
MOD = 998244353
k = len(str(N))

# (10**k)**n - 1 / 10**k - 1 をMODで割ったあまりを求めればいい
# それぞれMODで割る → a / b → bの逆元を考える

a = (pow(10, k*N, MOD) - 1) % MOD
b = (pow(10, k, MOD) - 1) % MOD

c = pow(b, MOD - 2, MOD)  # bの逆元

print(N*a*c % MOD)