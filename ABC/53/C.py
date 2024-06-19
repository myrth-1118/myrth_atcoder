x = int(input())
a = (x - 1) // 11

if  x - a*11 >= 7:
  print(a*2 + 2)

else:
  print(a*2 + 1)