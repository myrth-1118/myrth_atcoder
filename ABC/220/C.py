N = int(input())
A = list(map(int,input().split()))
X = int(input())
A_sum = sum(A)
dis = X
num = 0
ans = 0

if A_sum < X:
  dis = X % A_sum
  ans = N*(X // A_sum)
  
for i in A:
  num += i
  ans += 1 
  if num > dis:
    print(ans)
    break