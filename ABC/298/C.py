from collections import defaultdict
N = int(input())
Q = int(input())
box = defaultdict(list)
card = defaultdict(set)

for _ in range(Q):
  n, i, *j = map(int,input().split())

  if n == 1:
    J = j[0]
    box[J].append(i)
    card[i].add(J)
  
  elif n == 2:
    print(*sorted(box[i]))
  
  else:
    print(*sorted(card[i]))