N, X, Y = map(int,input().split())
ans = 0
num = 1

while N != 1:
  ans += X*num
  num += ans
  ans *= Y
  N -= 1
  
print(ans)