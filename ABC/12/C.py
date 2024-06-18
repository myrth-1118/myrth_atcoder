N = int(input())
a = 2025 - N

for i in range(1,10):
  for j in range(1,10):
    if i*j == a:
      print(i,'x',j)