import itertools  # 順列全探索
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
num = 0
P_n = 0
Q_n = 0

arr = list(range(1,N + 1))
arr_list = list(itertools.permutations(arr))

for ptn in arr_list:
  f = True
  num += 1
  for i in range(N):   # Pがptnと等しいか
    if P[i] != ptn[i]:
      f = False
  if f == True:
    P_n = num
    
  f = True
  for j in range(N):   # Qがptnと等しいか
    if Q[j] != ptn[j]:
      f = False
  if f == True:
    Q_n = num

print(abs(P_n - Q_n))