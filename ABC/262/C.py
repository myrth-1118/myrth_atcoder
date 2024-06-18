N = int(input())
a = list(map(int,input().split()))
node = [0]*(N + 1)
num_1 = 0
num_2 = 0

for i in range(N):
  if i + 1 == a[i]:
    num_1 += 1
  else:
    node[i + 1] = a[i]

for i in range(1, N + 1):
  if i == node[node[i]]:
    num_2 += 1

x = num_1*(num_1 - 1) // 2
y = num_2 // 2

print(x + y)