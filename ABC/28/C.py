N = list(map(int,input().split()))
num = []
for i in range(3):
  for j in range(i + 1,4):
    for k in range(j + 1,5):
      x = N[i] + N[j] + N[k]
      num.append(x)

num_sort = sorted(num)

print(num_sort[-3])