N, M = map(int,input().split())
a = N - M
b = 2**M

print((a*100 + M*1900)*b)