N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# AとBを結合してソートしたもののM番目が答え
# X[M - 1]がAの値だったらそのまま、Bの値だったら+1する
# Bの値を先に全て+1してからAと結合する
for i in range(M):
  B[i] += 1

X = A + B
X.sort()

print(X[M - 1])