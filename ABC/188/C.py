N = int(input())
A = list(map(int,input().split()))

x = max(A[:2**(N - 1)])
y = max(A[2**(N - 1):])

if x > y:
  num = y
else:
  num = x

print(A.index(num) + 1)