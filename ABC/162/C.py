import math
K = int(input())
num = 0

for i in range(1,K + 1):
  for j in range(1,K + 1):
    for k in range(1,K + 1):
      num += math.gcd(i,j,k)

print(num)