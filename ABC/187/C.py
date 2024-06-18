from collections import defaultdict
N = int(input())
check = defaultdict(int)
check1 = defaultdict(int)

for i in range(N):
  S = input()
  T = S.replace('!','')
  if len(S) == len(T):     # !がないとき 
    check[T] += 1
  else:                    # !があるとき
    check1[T] += 1

for i in check:
  if check[i] > 0 and check1[i] > 0:
    print(i)
    exit()

print('satisfiable')