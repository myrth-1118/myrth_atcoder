from collections import defaultdict
S = input()
node = defaultdict(int)
num = 1

for i in range(len(S)):
  if S[i] == '(':
    num += 1
  
  elif S[i] == ')':
    for j in node:
      if node[j] == num:
        node[j] = 0
    num -= 1
    
  else:
    if node[S[i]] != 0:
      print('No')
      exit()
    else:
      node[S[i]] = num

print('Yes')