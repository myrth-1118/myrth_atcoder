N = int(input())
S = input()
Q = int(input())
node = []
num = 0

for i in range(N*2):
  node.append(S[i])

for i in range(Q):
  T, A, B = map(int,input().split())
  
  if T == 1:
    node[(A + num*N - 1) % (2*N)], node[(B + num*N - 1) % (2*N)] = node[(B + num*N - 1) % (2*N)], node[(A + num*N - 1) % (2*N)]
  else:
    num += 1

if num % 2 == 0:
  print(''.join(node))

else:
  print(''.join(node[N:] + node[:N]))