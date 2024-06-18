# nCr 逆元
import math
W, H = map(int,input().split()) # 横W 縦H
a = math.factorial(W + H - 2)   # factorial(i) iの階乗 i*(i-1)*(i-2)*・・・*1
b = math.factorial(W - 1)
c = math.factorial(H - 1)
mod = 10**9 + 7

# pow(i,mod - 2,mod) iの逆元  本来a/b*cだが、xはb*cの逆元だからa*xで良い
x = pow(b*c % mod,mod - 2,mod) 
print(a*x % mod)