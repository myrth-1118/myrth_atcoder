import math
X = int(input())

def prime(n):
  if n % 2 == 0:
    return False
  for j in range(2, int(math.sqrt(n) + 1)):
    if n % j == 0:
      return False
  return True

if X == 2:
  print(X)
else:
  for i in range(10**5):
    if prime(X + i):
      print(X + i)
      exit()