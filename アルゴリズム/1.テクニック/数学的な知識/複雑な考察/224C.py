N = int(input())
A = []
num = 0

for i in range(N):
  x, y = map(int,input().split())
  A.append((x, y))

for i in range(N - 2):
  for j in range(i + 1, N -1):
    for k in range(j + 1, N):
      if A[j][0] == A[i][0] or A[k][0] == A[i][0] or A[k][0] == A[j][0]:
        if A[i][0] == A[j][0] == A[k][0]:
          continue
        else:
          num += 1
          
      else:
        a = (A[j][1] - A[i][1]) / (A[j][0] - A[i][0])
        b = (A[k][1] - A[i][1]) / (A[k][0] - A[i][0])
        c = (A[k][1] - A[j][1]) / (A[k][0] - A[j][0])
        if a == b == c:
          continue
        else:
          num += 1
          
print(num)