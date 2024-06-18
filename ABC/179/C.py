N = int(input())
num = 0

for i in range(1,N):
  a = N // i
  if a*i == N:
    num += a - 1
  else:
    num += a

print(num)