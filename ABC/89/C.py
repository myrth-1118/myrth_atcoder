N = int(input())
check = ['M','A','R','C','H']
num = [0]*5
ans = 0

for i in range(N):
  S = input()
  for i in range(5):     # defaultdictだと以降の3重ループが難しいためnumに回数を格納
    if S[0] == check[i]:
      num[i] += 1

for i in range(3):
  for j in range(i + 1,4):
    for k in range(j + 1,5):
      ans += num[i]*num[j]*num[k]

print(ans)