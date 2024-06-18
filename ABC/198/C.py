R, X, Y = map(int,input().split())
a = X**2 + Y**2

if a < R**2:
  print(2)
  exit()

num = 0

while (num*R)**2 < a:
  num += 1

print(num)