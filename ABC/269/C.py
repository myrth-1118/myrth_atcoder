# bit全探索
import itertools
import copy
N = int(input())
A = []
num = N
node = []   # N(2)の1のindex

if N == 0:
  print(0)
  exit()

while num != 0:
  A.append(num % 2)
  num //= 2

A.reverse()
for i in range(len(A)):
  if A[i] == 1:
    node.append(i)

arr_list = itertools.product((0,1), repeat=len(node))

for ptn in arr_list:
  B = copy.deepcopy(A)
  
  for i in range(len(node)):
    if ptn[i] == 0:
      B[node[i]] = 0

  ans = ''.join(map(str,B))  # int型を繋げて返す
  print(int(ans,2))          # 2進数を10進数に変換