X, A, D, N = map(int,input().split())

if D < 0:  # 数列を昇順に変更
  X = A*2 - X
  D = -D

if X <= A:
  ans = A - X
  
elif X >= A + D*(N - 1):
  ans = X - A - D*(N - 1)
  
else:
  ans = min((X - A) % D, D - ((X - A) % D))

print(ans)