N, K = map(int,input().split())
A = list(map(int,input().split()))
a = sorted(set(A))

if len(a) < K:
  for i in range(len(a)):
    if a[i] != i:
      print(i)
      exit()
      
  print(len(a))
      
else:
  for i in range(K):
    if a[i] != i:
      print(i)
      exit()
  
  print(K)