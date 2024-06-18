N, A, B = map(int,input().split())
P, Q, R, S = map(int,input().split())

# ×印の左上がnum1、右下がnum2、右上がnum3、左下がnum4
num1 = max(1 - A, 1 - B)
num2 = min(N - A, N - B)
num3 = max(1 - A, B - N)
num4 = min(N - A, B - 1)

for i in range(P, Q + 1):
  ans = []
  for j in range(R, S + 1):
    dx, dy = i - A, j - B
    if dx == dy and dx >= 0 and dx <= num2: # 右下の処理
      ans.append('#')
    elif dx == -dy and dx >= 0 and dx <= num4: # 左下の処理
      ans.append('#')
    elif -dx == dy and dy >= 0 and dx >= num3: # 右上の処理
      ans.append('#')
    elif dx == dy and dx <= 0 and dx >= num1: # 左上の処理
      ans.append('#')
    else:
      ans.append('.')

  print(''.join(ans))