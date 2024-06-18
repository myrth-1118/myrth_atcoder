import math
N = int(input())
a = round(math.pow(N,1/3)) # math.pow(N,1/3) Nの3乗根

def reverse(x):
  return int(str(x)[::-1])

for i in range(a,0,-1):
  if i**3 == reverse(i**3) and i**3 <= N:
    print(i**3)
    break