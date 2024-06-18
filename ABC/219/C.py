from collections import defaultdict
X = input()
N = int(input())
moji = defaultdict(int)
check = []

for i in range(len(X)):
  moji[X[i]] = i + 1

for _ in range(N):
  S = input()
  A = []
  for j in range(len(S)):
    A.append(moji[S[j]])
  
  check.append((A,S))

for _, name in sorted(check):
  print(name)