from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
node = defaultdict(int)
num = []

for i in A:
  if node[i] == 1:
    num.append(i)
    node[i] = 0
  else:
    node[i] += 1

num.sort()

if len(num) <= 1:
  print(0)

else:
  print(num[-1]*num[-2])