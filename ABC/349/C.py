S = input()
T = input()
A = T.lower() # lower() 大文字を小文字に変換
n = 0
ans = 'No'

for i in range(len(S)):
  if n == 0 and S[i] == A[0]:
     n = 1
  elif n == 1 and S[i] == A[1] and A[2] == 'x':
    ans = 'Yes'
    break 
  elif n == 1 and S[i] == A[1]:
    n = 2                     
  elif n == 2 and S[i] == A[2]:
    ans = 'Yes'
    break

print(ans)