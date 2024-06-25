# エラトステネスの篩
A, B, C, D = map(int,input().split())

# prime_listで1～200までの素数のリストを作成(エラトステネスの篩)
prime = [True]*(201)
prime_list = []
prime[0], prime[1] = False, False
for i in range(16):
  if prime[i]:
    for j in range(2, 200 // i + 1):
      prime[i*j] = False
for i, flag in enumerate(prime):
  if flag:
    prime_list.append(i)



for i in range(A, B + 1):
  flag = True
  for j in range(C, D + 1):
    if i + j in prime_list:
      flag = False
  
  if flag:
    print('Takahashi')
    exit()

print('Aoki')