import math
A, B, C, D = map(int,input().split())
c1, c2 = (A - 1) // C, B // C
d1, d2 = (A - 1) // D, B // D

X = math.lcm(C, D) # CとDの最小公倍数
x1, x2 = (A - 1) // X, B // X

c, d, x = c2 - c1, d2 - d1, x2 - x1

num = B - A + 1
num1 = c + d - x

print(num - num1)