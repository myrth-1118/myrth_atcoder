N = int(input())
A = list(map(int,input().split()))
x = sum(A) // N
y = x + 1
num1, num2 = 0, 0

for i in A:
  if x > i:
    num1 += x - i
  elif y < i:
    num2 += i - y

print(max(num1, num2))