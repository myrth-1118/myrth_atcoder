S = input()
check = 'WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW'
ans = ('Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si')
num = 0

for i in range(15):
  if check[i] == 'W':
    num += 1
  if S == check[i:20 + i]:
    print(ans[num - 1])
    exit()