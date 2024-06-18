N = int(input())
A = []
B = []
C = []

for i in range(N):
  A_n, B_n = map(int,input().split())
  A.append(A_n)
  B.append(B_n)
  C.append(B_n - A_n)

print(sum(A) + max(C))