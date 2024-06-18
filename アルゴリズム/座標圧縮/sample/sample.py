# 座標圧縮 具体例

N = 6
a = [10,8,6,4,2,5000]

p = sorted(set(a))
x = {num : i for i, num in enumerate(p)}
print(x)
# {2: 0, 4: 1, 6: 2, 8: 3, 10: 4, 5000: 5}

for i in range(N):
  print(x[a[i]])
# 4,3,2,1,0,5