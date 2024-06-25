N = int(input())
a = (N // 5) % 6 + 1
node = []

for i in range(6):
  node.append(str(((a - 1 + i) % 6 + 1)))

for i in range(N % 5):
  node[i], node[i + 1] = node[i + 1], node[i]

print(''.join(node))