# 転置行列
H, W = map(int,input().split())
A = []
B = []

for _ in range(H):
  S = list(input())
  A.append(S)
  
for _ in range(H):
  T = list(input())
  B.append(T)

x = list(zip(*A))  # 転置(行と列の入れ替え)したものをリストで返す(中身はtuple)
y = list(zip(*B))

for i, j in zip(sorted(x),sorted(y)):
  if i != j:
    print('No')
    exit()

print('Yes')