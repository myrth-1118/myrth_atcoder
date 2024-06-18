N, M = map(int,input().split())
A = list(map(int,input().split()))
score = []
yet = []

for i in range(N):
  S = input()
  num = i + 1
  yet1 = []
  
  for j in range(M):
    if S[j] == 'x':
      yet1.append(A[j])
    
    else:
      num += A[j]
  score.append(num)
  yet.append(sorted(yet1,reverse=True))

for i in range(N):
  a = max(score) - score[i]
  num = 0
  plus = 0
  
  if a == 0:
    print(0)
  else:
    for j in yet[i]:
      plus += j
      num += 1
      if a <= plus:
        print(num)
        break