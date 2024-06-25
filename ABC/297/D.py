A, B = map(int,input().split())
num = 0

while A != B:
  A, B = max(A, B), min(A, B)
  if A % B == 0:
    num += (A - B) // B
    print(num)
    exit()
  elif B*2 > A:
    A = A - B
    num += 1
  else:
    num += A // B
    A = A % B

print(num)