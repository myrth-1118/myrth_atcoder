N = list(map(int,input().split()))
A = sorted(N)
num = 0

a = A[0]
b = A[1]
c = A[2]
num += c - b    # +1する回数

if (a + c - b) % 2 == c % 2:  # aを×2するとき
  num += (b - a) // 2
else:                         # aを×2,bとcを+1するとき
  num += (b - a + 1) // 2 + 1

print(num)