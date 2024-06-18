import sys
sys.setrecursionlimit(10000)   # 再帰回数の上限設定
N, M = map(int,input().split())
road = [[] for i in range(N + 1)]  # N+1まで必要
ans = 0

for i in range(M):    # 道路で繋がっている都市のリスト
  A, B = map(int,input().split())
  road[A].append(B)
  
def dfs(s):           # 深さ優先探索
  if goal[s]:         # Trueのときは前に戻る 例(1回目→0回目　2回目→1回目)
    return
  goal[s] = True
  for p in road[s]:   # sと連結しているもの全てにdfs()を行う
    dfs(p)

for i in range(1,N + 1):  # スタート地点
  goal = [False]*(N + 1)   
  dfs(i)
  ans += sum(goal)        # Trueのみカウント

print(ans)