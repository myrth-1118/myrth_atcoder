N, M = map(int,input().split())
S = input()
T = 0     # 追加で必要枚数
num = 0
ans = 0 

for i in range(N):
  if S[i] == '2':
    T += 1
  elif S[i] == '1':
    num += 1
    if num > M:
      T += 1
  else:
    ans = max(ans,T)
    T = 0
    num = 0

ans = max(ans,T)
print(ans)