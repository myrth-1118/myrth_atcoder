X, K, D = map(int,input().split())

if X >= 0:
  if X - K*D >= 0:
    print(X - K*D)
    exit()
  
  num = (X - 1) // D + 1
  a, b = abs(X - num*D), abs(X - (num - 1)*D)
  H = num
  if a > b:
    H -= 1
    if H % 2 == K % 2:
      print(b)
    else:
      print(a)
        
  else:
    if H % 2 == K % 2:
      print(a)
    else:
      print(b)
  
else:
  if X + K*D <= 0:
    print(abs(X + K*D))
    exit()

  num = abs(X + 1) // D + 1
  a, b = abs(X + num*D), abs(X + (num - 1)*D)
  H = num
  if a > b:
    H -= 1
    if H % 2 == K % 2:
      print(b)
    else:
      print(a)
    
  else:
    if H % 2 == K % 2:
      print(a)
    else:
      print(b)