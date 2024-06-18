N = int(input())
X = list(map(int,input().split()))
node = sorted(X)
a = node[N // 2]
b = node[(N // 2) - 1]

for i in X:
  if i >= a:
    print(b)

  else:
    print(a)