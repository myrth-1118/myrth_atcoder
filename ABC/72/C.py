N = int(input())
a = list(map(int,input().split()))
node = [0]*(10**5 + 2)    # 範囲は-1から10**5

for i in a:
  node[i] += 1
  node[i + 1] += 1
  node[i + 2] += 1

print(max(node))