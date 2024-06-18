N = int(input())
p = list(map(int,input().split()))
A = [0]*N

for i in range(N):
  A[p[i] - 1] = i + 1

print(*A)