N = int(input())
S = input()
a = S[0]
num = 1

for i in range(1,N):
  if S[i] != a:
    num += 1
    a = S[i]

print(num)