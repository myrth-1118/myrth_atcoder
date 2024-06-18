from collections import defaultdict
N = int(input())
num = defaultdict(int)

for i in range(N):
  S = input()
  num[S] += 1
  if num[S] == 1:
    print(S)
  else:
    A = [S,'(',str(num[S] - 1),')']
    print(''.join(A))