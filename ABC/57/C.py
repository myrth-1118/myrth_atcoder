import math
N = int(input())
num = len(str(N))

for i in range(1,int(math.sqrt(N) + 1)):
  if N % i == 0:
    num = min(num,len(str(N // i)))

print(num)