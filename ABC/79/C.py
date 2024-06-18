A, B, C, D = input()

for i in range(2**3): # bit全探索
  op = ['-']*3
  for j in range(3):
    if (i >> j) & 1:         # i >> j  iを2進数表記し、j回右にずらしたとの一番右の数
      op[3 - 1 - j] = '+'
      
  x = A + op[0] + B + op[1] + C + op[2] + D
  S = eval(x)                               # eval() 文字列の式を計算できる
  
  if S == 7:
    print(x + '=7')
    break