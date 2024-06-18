N = int(input())
num = 0
total = 0
n_count = 0

for i in range(1,100):
  if total < N:
    num += i
    total += num
    n_count += 1 
  else:
    new_N = N - total + num
    break

n1 = ['1']*(n_count)
x = int(''.join(n1)) # 1つ目の数字
n_count = 0
total = 0

for i in range(1,100):
  if total < new_N:
    total += i
    n_count += 1 
  else:
    n3 = new_N - total + i - 1
    break

n2 = ['1']*(n_count)
y = int(''.join(n2)) # 2つ目の数字

n3 = ['1']*(n3)
z = int(''.join(n3)) # 3つ目の数字

print(x + y + z)