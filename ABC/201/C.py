S = input()
ans = 0

for i in range(10000):
  i_str = str(i)
  num = i_str.zfill(4)
  Flag = True
  node = []
  for j in range(4):
    node.append(int(num[j]))
    
  for k in range(10):
    if S[k] == 'o' and k not in node:
      Flag = False
    elif S[k] == 'x' and k in node:
      Flag = False
  if Flag:
    ans += 1

print(ans)