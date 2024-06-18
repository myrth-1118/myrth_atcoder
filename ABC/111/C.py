from collections import defaultdict
n = int(input())
v = list(map(int,input().split()))
node1, node2 = defaultdict(int), defaultdict(int)
check1, check2 = [], []
ans = 0

for i in range(n):
  if i % 2 == 0:
    node1[v[i]] += 1
  else:
    node2[v[i]] += 1

for i in node1:
  check1.append((node1[i],i))

for i in node2:
  check2.append((node2[i],i))

check1.sort(reverse=True)
check2.sort(reverse=True)

P, Q = check1[0][0], check2[0][0]   # 1番目に多い個数

if check1[0][1] != check2[0][1]:    # 1番多い個数の数字が異なるとき
  ans = n - P - Q

else:
  if len(check1) == 1 and len(check2) == 1:
    ans = n // 2
  elif len(check1) == 1:
    ans = n // 2 - check2[1][0]
  elif len(check2) == 1:
    ans = n // 2 - check1[1][0]
  else:
    a, b = P + check2[1][0], Q + check1[1][0]
    if a >= b:
      ans = n - a
    else:
      ans = n - b

print(ans)