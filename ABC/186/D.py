N = int(input())
A = list(map(int,input().split()))
A.sort()
x = 0

# ２つの数の最大値の二重和
for i in range(N):
  x += A[i]*i

A.sort(reverse=True)
y = 0

# ２つの数の最小値の二重和
for i in range(N):
  y += A[i]*i

print(x - y)