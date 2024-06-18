# 座標圧縮
H, W, N = map(int,input().split())
tate, yoko = [], []
for i in range(N):
  A, B = map(int,input().split())
  tate.append(A)
  yoko.append(B)

x = sorted(set(tate))
y = sorted(set(yoko))

X = {num : i + 1 for i, num in enumerate(x)}   # 最初のiは0のため+1する
Y = {num : i + 1 for i, num in enumerate(y)}

for i in range(N):
  print(X[tate[i]], Y[yoko[i]])