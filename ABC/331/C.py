from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
a = sorted(set(A))
temp = sum(A)

count_dict = defaultdict(int)  # 初期値0の辞書
ans_dict = defaultdict(int)

for i in A:          # 各数字の個数をcount_dictに入れる
  count_dict[i] += 1

for i in a:          # 各数字の答えをans_dictに入れる
  ans_dict[i] = temp - count_dict[i]*i
  temp = ans_dict[i]

for i in A:
  print(ans_dict[i],end=' ')