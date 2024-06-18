# 再帰関数
from functools import cache

@cache
def f(N):
  if N == 1:
    return 0
    
  else:
    return f(N // 2) + f((N + 1) // 2) + N

N = int(input())

print(f(N))