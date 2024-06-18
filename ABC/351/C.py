N = int(input())
A = list(map(int,input().split()))
P = []
Flag = True
for i in range(N):
  Flag = True
  P.append(A[i])
  #長さが1でないとき
  if (len(P)) != 1:
    while P[len(P)-1] == P[len(P)-2] and Flag == True:
      P[len(P)-1] += 1
      P.pop(len(P)-2)
      if len(P) == 1:
        Flag = False
  else:
    continue
print(len(P))