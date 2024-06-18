import math
N, K = map(int,input().split())
A = list(map(int,input().split()))
B = []

for i in range(len(A)):
  if A[i] <= K:
    B.append(A[i])

B_set = set(B)
x =  K*(K + 1) // 2 - sum(B_set)
print(math.floor(x))