from itertools import product     # bit全探索
A, B, C, D = input()

for pro in product((0,1),repeat=3):   # 0と1から成る長さ3の組み合わせの全列挙
  op = ['-']*3                        # 記録の初期化
  for i in range(3): 
    if pro[i] == 1:
      op[i] = '+'

  x = A + op[0] + B + op[1] + C + op[2] + D
  S = eval(x)                               # eval() 文字列の式を計算できる
   
  if S == 7:
    print(x + '=7')
    break