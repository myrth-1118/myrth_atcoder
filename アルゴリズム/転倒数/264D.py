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

S = input()
node = ['a', 't', 'c', 'o', 'd', 'e', 'r']
# checkにnodeと対応する座標と格納
check = []

for i in range(7):
  for j in range(7):
    if S[i] == node[j]:
      check.append(j + 1)

ans = Inversion_Number_By_BIT(check)
print(ans)