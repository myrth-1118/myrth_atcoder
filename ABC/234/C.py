K = int(input())
A = []
a = bin(K)[2:]

for i in range(len(a)):
  if a[i] == '1':
    A.append('2')
  else:
    A.append('0')

print(''.join(A))