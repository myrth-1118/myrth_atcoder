# 2数の積の二重和
N = 4
A = [2,3,5,8] 
# 愚直解 2*3 + 2*5 + 2*8 + 3*5 + 3*8 + 5*8 = 6+10+16 + 15+24 + 40 = 111

# 累積和 a*b + a*c + a*d + b*c + b*d + c*d = a*(b+c+d) + b*(c+d) +c*(d)
node = [0]*(N + 1)
for i in range(N): # Aの累積和の作成
  node[i + 1] += node[i] + A[i]
# node = [0,2,5,10,18]

y = 0
for i in range(1,N):  # 2数の積の累積和
  y += A[i - 1]*(node[-1] - node[i])
  print(y)
# i=1 y=(18-2)*2=32, i=2 y=(18-5)*3+32=71, i=3 y=(18-10)*5+71=111  y=111


# 2数のmaxの二重和
# 愚直解 3 + 5 + 8 + 5 + 8 + 8
# 2*0 + 3*1 + 5*2 + 8*3
x = 0
for i in range(N):
  x += A[i]*i
  print(x)

