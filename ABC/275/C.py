import itertools
S = [input() for _ in range(9)]
ans = 0

# 純粋な正方形の確認
tate = itertools.combinations(range(9),2)
for ptn1 in tate:
  a = ptn1[0]
  b = ptn1[1]
  
  yoko = itertools.combinations(range(9),2)
  for ptn2 in yoko:
    c = ptn2[0]
    d = ptn2[1]
    
    if b - a == d - c and S[a][c] == S[a][d] == S[b][c] == S[b][d] == '#':
      ans += 1

# 斜めの正方形の確認
# 一番上の頂点の座標
for i in range(7):
  for j in range(1,8):
    # 一番左の頂点の座標
    for k in range(i + 1, 8):
      for l in range(j):
        p, q, r, s = k + j - l, l + k - i, j - l + i, k - i + j
        if 0 <= p < 9 and 0 <= q < 9 and 0 <= r < 9 and 0 <= s < 9:
          if S[i][j] == S[k][l] == S[p][q] == S[r][s] == '#':
            ans += 1

print(ans)