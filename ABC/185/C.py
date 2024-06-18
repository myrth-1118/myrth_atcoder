import math
L = int(input())

a = math.factorial(L - 1)
b = math.factorial(11)
c = math.factorial(L - 12)

print(a // (b*c))