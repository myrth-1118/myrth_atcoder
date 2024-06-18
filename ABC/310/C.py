from collections import defaultdict
N = int(input())
data = defaultdict(int)
num = 0

for _ in range(N):
  S = input()
  S_reversed = ''.join(list(reversed(S)))
  if data[S] == 0 and data[S_reversed] == 0:
    data[S] = 1
    num += 1

print(num)