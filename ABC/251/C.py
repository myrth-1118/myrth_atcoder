from collections import defaultdict
N = int(input())
score = defaultdict(int)
num = 0

for i in range(N):
  S, T = map(str,input().split())
  if score[S] == 0:
    score[S] = 1
    if num < int(T):
      num = int(T)
      ans = i + 1

print(ans)