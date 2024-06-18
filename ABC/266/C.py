# 外積
Ax, Ay = map(int,input().split())
Bx, By = map(int,input().split())
Cx, Cy = map(int,input().split())
Dx, Dy = map(int,input().split())
ans = 'Yes'

if (Ay - By)*(Cx - Bx) - (Ax - Bx)*(Cy - By) <= 0:
  ans = 'No'

if (By - Cy)*(Dx - Cx) - (Bx - Cx)*(Dy - Cy) <= 0:
  ans = 'No'
  
if (Cy - Dy)*(Ax - Dx) - (Cx - Dx)*(Ay - Dy) <= 0:
  ans = 'No'

if (Dy - Ay)*(Bx - Ax) - (Dx - Ax)*(By - Ay) <= 0:
  ans = 'No'

print(ans)