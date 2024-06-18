N, K = map(int,input().split())
H = list(map(int,input().split()))
H.sort(reverse=True)

a = sum(H[:K])
b = sum(H)

print(b - a)