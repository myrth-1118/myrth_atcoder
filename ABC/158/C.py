A, B = map(int,input().split())
N = B*10

for i in range(100):
  if (N + i) // 10 == B:
    if int((N + i)*0.08) == A:
      print(N + i)
      break
  else:
    print(-1)
    break