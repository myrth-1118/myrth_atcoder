# 平面走査
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = sorted(set(A))
b = sorted(set(B))

r, ans = 0, 10**9
if len(b) == 1:
  for i in range(len(a)):
    ans = min(ans,abs(a[i] - b[0]))
    
else:
  for i in range(len(a)):
    while r + 1 != len(b) - 1 and a[i] > b[r + 1]:  # a[i] > b[r + 1]のときbが右端でなければr += 1できる
      r += 1
    ans = min(ans,abs(a[i] - b[r]),abs(a[i] - b[r + 1]))
    
print(ans)