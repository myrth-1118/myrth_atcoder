# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j

# 転倒数
class BIT:
    def __init__(self, n):
        self.size=n
        self.tree = [0] * (n+1)
    
    def add(self, i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        total = 0
        while i >0:
            total += self.tree[i]
            i -= i & -i
        
        return total

def Inversion_Number_By_BIT(A):
    ans = 0
    Bit = BIT(len(A))
    for i in range(len(A)):
        ans += i - Bit.sum(A[i])
        Bit.add(A[i], 1)
    return ans
    
N = int(input())
A = list(map(int,input().split()))
ans = Inversion_Number_By_BIT(A)
print(ans)