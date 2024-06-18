N = int(input())
ans = []
num = 0
n = 0

while num < N:
  n += 1
  num += 26**n

for i in range(1, n + 1):
  N -= 1
  a = N % 26
  ans.append(chr(a + 1 + 96))
  N //= 26

print(''.join(ans[::-1]))