N = int(input())
s = [int(input()) for _ in range(N)]

S = sorted(s)

if sum(S) % 10 != 0:
  print(sum(S))
  exit()
  
else:
  for i in S:
    if i % 10 != 0:
      print(sum(S) - i)
      exit()

print(0)