# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_c

A, B = map(int,input().split())

for i in range(B - A, 0,-1):
  b = B // i
  a = ((A - 1) // i) + 1
  if b != a:
    print(i)
    exit()