# 深さ優先探索
# def()の内部でlistの変更は保存されるが、値の変更は保存されない
import sys
sys.setrecursionlimit(10**9)
N, M = map(int,input().split())
road = [[0]*(N + 1) for _ in range(N + 1)]
ans = 0
visited = [False]*(N + 1)

for _ in range(M):
  A, B, C = map(int,input().split())
  road[A][B] = C
  road[B][A] = C

def dfs(x, s): # x=現在地,s=道路の長さの合計
  global ans
  visited[x] = True
  if ans < s:
    ans = s
  
  for i in range(1, N + 1):
    if visited[i] == False and road[x][i] != 0:
      dfs(i, s + road[x][i])
  visited[x] = False           # 訪問したときにTrueにして、戻るときにFalseにする →別の道でも同じ街が通れる

for i in range(1, N + 1):
  dfs(i, 0)

print(ans)