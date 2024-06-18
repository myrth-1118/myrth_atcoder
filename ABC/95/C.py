A, B, C, X, Y = map(int,input().split())
ans = 0

if A + B <= C*2:
  ans = A*X + B*Y

else:
  ans += min(X,Y)*C*2
  
  if X >= Y:
    if A >= C*2:
      ans += C*(X - Y)*2
    else:
      ans += A*(X - Y)
  else:
    if B >= C*2:
      ans += C*(Y - X)*2
    else:
      ans += B*(Y - X)

print(ans)