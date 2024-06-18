S = input()
K = int(input())

for i in range(len(S)):
  a = int(S[i])
  
  if i + 1 == K:
    print(a)
    exit()
  elif a != 1:
    print(a)
    exit()