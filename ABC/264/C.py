# 順列全探索 組合せ重複なし 単調増加数列
import itertools
H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

H = H1 - H2
W = W1 - W2

# 横列の削除
for yoko in itertools.combinations(range(H1), H):
  row = []
  for i in range(H1):
    if i not in yoko:
      row.append(i)

  # 縦列の削除
  for tate in itertools.combinations(range(W1), W):
    col = []
    for i in range(W1):
      if i not in tate:
        col.append(i)

    # 削除した後に残った行列
    sub = [[A[r][c] for c in col] for r in row]

    if sub == B:
      print('Yes')
      exit()

print('No')