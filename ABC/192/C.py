N, K = map(int,input().split())
A = []
S = str(N)
ans = N

for i in range(K):
  if ans == 0:
    break
  else:
    for j in range(len(S)):          # 数字を１つずつAに格納
      A.append(S[j])

    A_max = sorted(A,reverse=True)   # 最大の数字
    A_min = sorted(A)                # 最小の数字
    a_max = ''.join(A_max)
    a_min = ''.join(A_min)
    ans = int(a_max) - int(a_min)    # n回目の答え
    S = str(ans)
    A.clear()

print(ans)