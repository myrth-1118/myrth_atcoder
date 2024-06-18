N = int(input())

def prime_factorize(n): # 素数列挙(試し割り法)
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

num = prime_factorize(N)
A = set(num)

print(A)  