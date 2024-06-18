N = int(input())
A = list(map(int,input().split()))

if sum(A) == (sum(set(A))):
  print('YES')
else:
  print('NO')