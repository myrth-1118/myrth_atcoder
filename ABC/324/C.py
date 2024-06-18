N, T = input().split()
A = int(N)
ans = []

for i in range(A):
  S = input()
  n = 0
  num = 0
  
  if S == T:
    ans.append(i + 1)
  
  elif len(S) == len(T) - 1:
    for j in range(len(S)):
      if T[n] == S[j]:
        n += 1
      elif num == 0 and T[n] != S[j] and T[n + 1] == S[j]:
        num = 1
        n += 2
      else:
        num = 2
        break
    if num <= 1:
      ans.append(i + 1)
  
  elif len(S) == len(T):
    for j in range(len(T)):
      if T[j] == S[n]:
        n += 1
      elif T[j] != S[n] and num == 0:
        num = 1
        n += 1
      else:
        num = 2
        break
    if num == 1:
      ans.append(i + 1)
  
  elif len(S) == len(T) + 1:
    for j in range(len(T)):
      if T[j] == S[n]:
        n += 1
      elif num == 0 and T[j] != S[n] and T[j] == S[n + 1]:
        num = 1
        n += 2
      else:
        num = 2
        break
    if num <= 1:
      ans.append(i + 1)

print(len(ans))
print(*ans)