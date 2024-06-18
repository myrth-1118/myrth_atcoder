N, T = map(int,input().split())
t = list(map(int,input().split()))
num = T

for i in range(N - 1):
  if t[i + 1] - t[i] <= T:
    num += t[i + 1] - t[i]
  else:
    num += T

print(num)