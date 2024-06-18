# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c
# 三井住友信託銀行プログラミングコンテスト2019

# 1次元DP
X = int(input())
node = [0]*101000

for i in range(1001):
  node[100*i] = 1

for i in range(1,6):
  for j in range(100001):
    if j % (100 + i) == 0:
      node[j] = 1
    elif 0 <= j - 100 - i <= 100000 and node[j - 100 - i] == 1:
      node[j] = 1

if node[X] == 1:
  print(1)
else:
  print(0)