N = int(input())
d = list(map(int,input().split()))
A = sorted(d)
ans = A[N // 2] - A[(N // 2) - 1]

print(ans)