# ランレングス圧縮
S = input()
T = input()

def run_length(x): #隣接する文字と数の取得
  num_list = []
  count = 1
  for i in range(len(x)):
    if i + 1 < len(x) and x[i] == x[i + 1]:
      count += 1
    else:
      num_list.append((x[i],count))
      count = 1
  
  return num_list

a, b = run_length(S), run_length(T)
ans = 'Yes'

if len(a) != len(b):
  ans = 'No'
else:
  for (s1,s2),(t1,t2) in zip(a,b):
    if s1 != t1:
      ans = 'No'
      break
    elif s2 != t2 and (s2 == 1 or s2 > t2):
      ans = 'No'
      break

print(ans)