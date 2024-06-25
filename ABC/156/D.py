# 繰り返し2乗法
# 逆元
n, a, b = map(int,input().split())
MOD = 10**9 + 7

# 繰り返し2乗法
# base=n乗するもの, exp=n乗
def mod_exp(base, exp, mod):
  result = 1
  while exp > 0:
    if exp % 2 == 1:
      result = (result*base) % mod
    base = (base*base) % mod
    exp //= 2
  return result

# nCrを求める
def combination(n, r, mod):
  result_n = 1
  result_d = 1
  # 分子の計算
  for i in range(r):
    result_n *= n - i
    result_n %= mod
  # 分母の計算
  for i in range(r):
    result_d *= i + 1
    result_d %= mod
  # 逆元の計算
  x = pow(result_d % mod, mod - 2, mod)
  return result_n*x % mod

# 組合せの総数
p = (mod_exp(2, n, MOD) - 1) % MOD

num_a = combination(n, a, MOD)
num_b = combination(n, b, MOD)

print((p - num_a - num_b) % MOD)