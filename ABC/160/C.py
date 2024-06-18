K, N = map(int,input().split())
A = list(map(int,input().split()))
dis = 0

for i in range(0,N - 1):
  dis = max(dis,A[i + 1] - A[i])

dis = max(dis,A[0] + K - A[-1])  # 原点を含むものの確認

print(K - dis)