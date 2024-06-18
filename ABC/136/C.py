N = int(input())
H = list(map(int,input().split()))
num = 0

for i in range(N - 1):
  if H[i] > H[i + 1]:
    if H[i] - H[i + 1] == 1 and num <= H[i + 1]:
      num = H[i + 1]
    else:
      print('No')
      exit()

print('Yes')