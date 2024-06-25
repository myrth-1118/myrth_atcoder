Sx, Sy = map(int,input().split())
Tx, Ty = map(int,input().split())
ans = 0

if Sy % 2 == 0 and Sx % 2 == 0:
  Sx += 1
elif Sy % 2 == 1 and Sx % 2 == 1:
  Sx += 1

if Ty % 2 == 0 and Tx % 2 == 0:
  Tx += 1
elif Ty % 2 == 1 and Tx % 2 == 1:
  Tx += 1

a, b = abs(Tx - Sx), abs(Ty - Sy)
ans += min(a, b)

if a < b:
  ans += b - a
else:
  if Sx < Tx:
    ans += (Tx - (Sx + b)) // 2
  else:
    ans += (Sx - b - Tx) // 2

print(ans)