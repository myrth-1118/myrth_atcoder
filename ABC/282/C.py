N = int(input())
S = list(input())
flag = False

for i in range(N):
  if flag == False and S[i] == '"':
    flag = True
  elif flag == True and S[i] == '"':
    flag = False
  elif flag == False and S[i] == ',':
    S[i] = '.'

print(''.join(S))