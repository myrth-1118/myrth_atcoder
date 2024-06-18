# 尺取り法
N = int(input())
A = list(map(int,input().split()))
x = 10**8
A_total = sum(A)
A.sort()

r, ans, num = N - 1, 0, 0                     # r=右端 num=条件を満たす数の合計 
for i in range(N):                            # i=左端
  while A[i] + A[r] >= x and i != r - 1:      # iとrが同じにならないように調整
    r -= 1
    num += 1
  ans += num 
  
  if i == r - 1:
    if A[i] + A[r] >= x:
      ans += 1 
    num += 1
    ans += (num*(num - 1)) // 2               # 2つとも5×10**7以上の数字の組合せ
    break

print(A_total*(N - 1) - ans*x)