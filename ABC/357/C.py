import copy
N = int(input())
node = [['#']*3 for _ in range(3)]
node[1][1] = '.'

if N == 0:
  print('#')
  exit()

if N >= 2:
  n = 1
  while n != N:
    n += 1
    A = copy.deepcopy(node)
    node = [['.']*3**n for _ in range(3**n)]
    for i in range(3):
      for j in range(3):
        if i == 1 and j == 1:
          pass
        else:
          for k in range(3**(n - 1)):
            for l in range(3**(n - 1)):
              node[i*(3**(n - 1)) + k][j*(3**(n - 1)) + l] = A[k][l]


for i in node:
  print(''.join(i))