c = [list(map(int,input().split())) for _ in range(3)]
ans = 'Yes'

a = c[0][1] - c[0][0]
b = c[0][2] - c[0][0]
p = c[1][0] - c[0][0]
q = c[2][0] - c[0][0]

for i in range(1,3):
  if a != c[i][1] - c[i][0]:
    ans = 'No'
  if b != c[i][2] - c[i][0]:
    ans = 'No'
  if p != c[1][i] - c[0][i]:
    ans = 'No'
  if q != c[2][i] - c[0][i]:
    ans = 'No'

print(ans)