N = int(input())
a = list(map(int,input().split()))
num1, num2, num4 = 0, 0, 0
ans = 'No'

for i in a:
  if i % 2 == 1:
    num1 += 1
  elif i % 4 == 0:
    num4 += 1
  else:
    num2 += 1

if num1 == 0:
  ans = 'Yes'
elif num2 == 0:
  if num1 - 1 <= num4:
    ans = 'Yes'
elif num1 <= num4:
  ans = 'Yes'

print(ans)