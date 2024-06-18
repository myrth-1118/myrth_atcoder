# 累積和
N = int(input())
S = input()
num_E = [0]*(N + 1)
num_W = [0]*(N + 1)
ans = 10**6

for i in range(N):
  if S[i] == 'E':
    num_E[i + 1] = num_E[i] + 1
    num_W[i + 1] = num_W[i]
  
  else:
    num_W[i + 1] = num_W[i] + 1
    num_E[i + 1] = num_E[i]

for i in range(N):
  ans = min(ans,num_W[i] + num_E[-1] - num_E[i + 1])    # 向きを変える人の最小値

print(ans)