N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))
check = []

for i in A:
  for j in B:
    for k in C:
       check.append(i + j + k)

Z = set(check)

for i in X:       # リストの中にあるかの確認をfor文1回で済ませる
  if i in Z:
    print('Yes')
  else:
    print('No')