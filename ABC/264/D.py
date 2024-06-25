S = input()
node = ['a', 't', 'c', 'o', 'd', 'e', 'r']
check = []

for i in range(7):
  for j in range(7):
    if S[i] == node[j]:
      check.append(j + 1)

ans = 0
for i in range(7):
  if check[i] != i + 1:
    a = check.index(i + 1)
    for j in range(a - i):
      check[a - j], check[a - j - 1] = check[a - j - 1], check[a - j]
      ans += 1
      
print(ans)