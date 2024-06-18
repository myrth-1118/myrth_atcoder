import bisect
N = int(input())
L = list(map(int,input().split()))
L.sort()  # A = L.sort()とは書けない
ans = 0

for i in range(2,N):   # 1番目に大きい辺
  for j in range(1,i): # 2番目に大きい辺
    x = bisect.bisect_right(L,L[i]-L[j])     # L[i]-L[j]より大きい数字のindexを教えてくれる
    
    ans += max(0,j - x)                      # j-x<0のときはjが一番小さくなるため不可

print(ans)