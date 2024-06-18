A, B, C = map(int,input().split())
num = C % 2

if num == 0:
  if abs(A) == abs(B):
    print('=')
  elif abs(A) > abs(B):
    print('>')
  else:
    print('<')
else:
  if A == B:
    print('=')
  elif A > B:
    print('>')
  else:
    print('<')