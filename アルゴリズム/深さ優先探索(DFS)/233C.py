# 深さ優先探索
N, X = map(int,input().split())
node, A = [], []
ans = 0
for _ in range(N):
  L, *a = list(map(int,input().split()))
  node.append(L)
  A.append(a)

def dfs(num , x):
  global ans
  
  for i in range(node[num]):
    
    if x*A[num][i] <= X:
      nx = x*A[num][i]
      
      if num + 1 == N:
        if nx == X:
          ans += 1
      else:
        dfs(num + 1, nx)   # 関数内でnum += 1とすると再帰後に値を戻せなくなる xも同様
        
dfs(0, 1)

print(ans)