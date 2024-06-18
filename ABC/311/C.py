# 深さ優先探索
import sys
sys.setrecursionlimit(10**9)
N = int(input())
A = list(map(int,input().split()))
node = [False]*N
check = 0
ans = []

def dfs(n, x):
  global check
  if node[n]:
    check = n
    return
  node[n] = True
  dfs(x - 1, A[x - 1])

def dfs1(n, x):
  global ans
  if node[n]:
    return
  node[n] = True
  ans.append(x)
  dfs1(x - 1, A[x - 1])

dfs(0, A[0])

node = [False]*N
dfs1(check, A[check])

print(len(ans))
print(*ans)