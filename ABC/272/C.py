N = int(input())
A = list(map(int,input().split()))
S = sorted(A,reverse=True)

if N == 2:
  if (S[0] + S[1]) % 2 != 0:
    print(-1)
    exit()
  else:
    print(sum(A))
    exit()  
else:
  a = S[0] + S[1]
  b = S[0] + S[2]
  c = S[1] + S[2] 

  if a % 2 == 0:
     ans = a
  else:
    if b % 2 == 0:
      ans = b
    else:
      ans = c

for i in range(1,N):          # このfor文がないと何故かWAになる
  if (S[0] + S[i]) % 2 == 0:
    ans = max(ans,S[0] + S[i])

print(ans)