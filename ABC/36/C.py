# 座標圧縮
N = int(input())
A = [int(input()) for _ in range(N)]

a = sorted(set(A))
B = {num : i for i, num in enumerate(a)}

for i in A:
  print(B[i])