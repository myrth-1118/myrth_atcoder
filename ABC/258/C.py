N, Q = map(int,input().split())
S = input()
num = 0

for i in range(Q):
  a, b = map(int,input().split())
  
  if a == 1:
    num += b
  else:
    print(S[(b - num - 1) % N])