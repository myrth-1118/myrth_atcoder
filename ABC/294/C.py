N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_num = 0
B_num = 0
A_ans = []
B_ans = []
j = 1

for i in range(1,N + M):
  a = A[A_num]
  b = B[B_num]
  
  if a > b:
    B_ans.append(i)
    if b != B[-1]:
      B_num += 1 
      
    else:
      while i + j < N + M + 1 :
        A_ans.append(i + j)
        j += 1
      break
  
  else:
    A_ans.append(i)
    if a != A[-1]:
      A_num += 1
      
    else:
      while i + j < N + M + 1:
        B_ans.append(i + j)
        j += 1
      break

print(*A_ans)
print(*B_ans)