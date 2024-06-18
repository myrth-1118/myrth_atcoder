N, M = map(int,input().split())
node = []
node1 = []
a = 1
num = 0
ans = 0
mod = 998244353

while a <= N:
  a *= 2
  num += 1

for i in range(num):
  a = 0
  x = 2**(i + 1)
  a += (N // x)*(x // 2)
  a += max(0,(N % x) + 1 - (x // 2))
  node.append(a)

b = M
while b != 0:
  node1.append(b % 2)
  b //= 2
  
for i in range(min(len(node),len(node1))):
  if node1[i] == 1:
    ans += node[i] % mod

print(ans % mod)