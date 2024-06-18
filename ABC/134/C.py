N = int(input())
A = [int(input()) for i in range(N)]
A_sort = sorted(A)
x = A_sort[-1]
y = A_sort[-2]

for i in A:
  if i == x:
    print(y)
  else:
    print(x)