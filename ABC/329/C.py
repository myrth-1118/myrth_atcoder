from collections import defaultdict
N = int(input())
S = input()
check = defaultdict(int)
num = 1
temp = 0  # 連続している文字
ans = 0

for i in range(N):
  if S[i] != temp:
    num = 1
    temp = S[i]
  else:
    num += 1
  
  check[temp] = max(check[temp],num)

for i in check:
  ans += check[i]

print(ans)