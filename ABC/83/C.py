X, Y = map(int,input().split())
num = 0

for i in range(2**100):
  if X*2**num <= Y:
    num += 1
  else:
    print(num)
    exit()