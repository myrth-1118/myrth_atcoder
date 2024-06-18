from collections import defaultdict
S = input()
T = input()
node_S, node_T = defaultdict(int), defaultdict(int)
check = []
sample = ['a', 't', 'c', 'o', 'd', 'e', 'r']
ans = 'Yes'

for i in range(len(S)):
  node_S[S[i]] += 1
  node_T[T[i]] += 1
  check.append(S[i])
  check.append(T[i])

num_S, num_T = node_S['@'], node_T['@']
node_S['@'], node_T['@'] = 0, 0

A = set(check)
A.discard('@')
s, t = 0, 0

for i in A:
  if i in sample:
    t += max(0,node_S[i] - node_T[i])
    s += max(0,node_T[i] - node_S[i])
  else:
    if node_S[i] != node_T[i]:
      ans = 'No'
      break

if num_S - s >= 0 and num_T - t >= 0 and num_S - s == num_T - t:
  pass
else:
  ans = 'No'

print(ans)