N = int(input())
T, num_x, num_y = 0, 0, 0
ans = 'Yes'

for i in range(N):
  t, x, y = map(int,input().split())
  a = abs(x - num_x) + abs(y - num_y)
  
  if a <= t - T and a % 2 == (t - T) % 2:
    T, num_x, num_y = t, x, y
    pass
  else:
    ans = 'No'
    break

print(ans)