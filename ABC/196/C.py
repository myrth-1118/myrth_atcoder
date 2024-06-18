N = int(input())    # 二分探索
l = 0
r = 1000000

while r - l > 1:
  m = (r + l) // 2
  if int(str(m)*2) > N:     # Nより大きいとき、rを左にずらす
    r = m
  elif int(str(m)*2) <= N:  # Nより小さいとき、lを右にずらす
    l = m

print(l)