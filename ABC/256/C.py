h1, h2, h3, w1, w2, w3 = map(int,input().split())
ans = 0

if h1 + h2 + h3 != w1 + w2 + w3:
  print(0)
  exit()

for i in range(1, min(h1, w1) - 1):
  A = i
  
  for j in range(1, h1 - A):
    B = j
    C = h1 - A - B
    
    for k in range(1, w1 - A):
      D = k
      G = w1 - A - D
      
      if w2 - B >= 2 and h2 - D >= 2:
        for l in range(1, min(w2 - B, h2 - D)):
          E = l
          F = h2 - D - E
          H = w2 - B - E
          
          if w3 - C - F == h3 - G - H and h3 - G - H >= 1:
            ans += 1

print(ans)