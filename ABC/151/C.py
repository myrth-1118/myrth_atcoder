N, M = map(int,input().split())
node = [0]*(N + 1)
num_AC = 0
num_WA = 0

for _ in range(M):
  p, S = map(str,input().split())
  P = int(p)
  if S == 'WA' and node[P] != -1:
    node[P] += 1
  elif S == 'AC' and node[P] != -1:
    num_AC += 1
    num_WA += node[P]
    node[P] = -1

print(num_AC, num_WA)