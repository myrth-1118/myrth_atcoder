# 累積和
N = int(input())
A = sorted(list(map(int,input().split())))
x = 0
y = 0
node = [0]*(N + 1)

for i in range(N):
  x += A[i]**2
  node[i + 1] += node[i] + A[i]
  
x *= N - 1

for i in range(1,N):  # 2数の積の累積和
  y += A[i - 1]*(node[-1] - node[i])

print(x - y*2)