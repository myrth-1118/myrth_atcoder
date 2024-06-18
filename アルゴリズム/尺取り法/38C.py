# 尺取り法
N = int(input())
a = list(map(int,input().split()))
a.append(0)                  # a[N - 1]とa[N]の比較をするため追加

r, ans, A = 0, 0, a[1]       # r=右端 A=右端の右側の数字
for i in range(N):
  while r < N and a[r] < A:
    r += 1
    A = a[r + 1]

  ans += r - i + 1
  
  if i == r and r !=  N - 1:
    r += 1
    A = a[r + 1]

print(ans)