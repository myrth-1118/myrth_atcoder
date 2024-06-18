N = int(input())
A = list(map(int,input().split()))
B = [0]*N

for i in A:
  B[i - 1] += 1
  
  if B[i - 1] == 2:
    print(i,end=' ')