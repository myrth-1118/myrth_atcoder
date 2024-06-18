W, H, x, y = map(int,input().split())
a = W*H / 2

if x*2 == W and y*2 == H:
  print(a, 1)
else:
  print(a, 0)