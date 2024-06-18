N, K = map(int,input().split())
a = list(map(int,input().split()))
x = K // N
y = K % N
a_sort = sorted(a)

if N == 1:
  print(K)
else:
  for i in a:
    if i <= a_sort[y - 1] and y != 0:
      print(x + 1)
    else:
      print(x)