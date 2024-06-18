N = int(input())
print(2*N + 1)

for i in range(N):
  aoki = int(input())
  if aoki % 2 == 1:
    print(aoki + 1)
  else:
    print(aoki - 1)