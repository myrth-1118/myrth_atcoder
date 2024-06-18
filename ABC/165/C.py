# 順列全探索 組合せ重複あり(単調増加数列) 1~10で長さ10だと92000通り
import itertools
N, M, Q = map(int,input().split())
H = []
ans = 0
for i in range(Q):
  Hi = list(map(int,input().split()))  # listを外すと15行目のループが動かない
  H.append(Hi)

#(1,1,1),(1,1,2),(1,1,3),(1,2,2),(1,2,3),(1,3,3),(2,2,2)・・・のように返す
arr_list = itertools.combinations_with_replacement(range(1,M + 1), N)

for ptn in arr_list:
  num = 0
  for a, b, c, d in H:
    if ptn[b - 1] - ptn[a - 1] == c:
      num += d
      
  ans = max(ans,num)

print(ans)