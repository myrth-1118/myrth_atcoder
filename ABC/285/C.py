S = input()
num = 0

for i in range(1,len(S) + 1):
  a = ord(S[-i])
  num += (a - 64)*26**(i - 1)
  
print(num)