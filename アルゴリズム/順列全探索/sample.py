import itertools

# ➀順列 重複あり 2**3通り bit全探索
arr_list = itertools.product((0,1), repeat=3)
for ptn in arr_list:
  print(ptn)
#(0, 0, 0) (0, 0, 1) (0, 1, 0) (0, 1, 1) 
#(1, 0, 0) (1, 0, 1) (1, 1, 0) (1, 1, 1)


# ➀順列全探索 順列重複あり 3**3通り
arr_list = itertools.product(range(1,4), repeat=3)
for ptn in arr_list:
  print(ptn)
#(1, 1, 1) (1, 1, 2) (1, 1, 3) (1, 2, 1) (1, 2, 2) (1, 2, 3) 
#(1, 3, 1) (1, 3, 2) (1, 3, 3) (2, 1, 1) (2, 1, 2) (2, 1, 3) 
#(2, 2, 1) (2, 2, 2) (2, 2, 3) (2, 3, 1) (2, 3, 2) (2, 3, 3) 
#(3, 1, 1) (3, 1, 2) (3, 1, 3) (3, 2, 1) (3, 2, 2) (3, 2, 3) 
#(3, 3, 1) (3, 3, 2) (3, 3, 3) 


# ➁順列全探索 順列重複なし 3×2×1通り 
arr_list = itertools.permutations(range(1,4),3)
for ptn in arr_list:
  print(ptn)
#(1, 2, 3) (1, 3, 2) (2, 1, 3) (2, 3, 1) (3, 1, 2) (3, 2, 1) 


# ➂順列全探索 組合せ重複あり 単調増加数列
arr_list = itertools.combinations_with_replacement(range(1,4),3)
for ptn in arr_list:
  print(ptn)
#(1, 1, 1) (1, 1, 2) (1, 1, 3) (1, 2, 2) (1, 2, 3) 
#(1, 3, 3) (2, 2, 2) (2, 2, 3) (2, 3, 3) (3, 3, 3) 


# ➃順列全探索 組合せ重複なし 単調増加数列
arr_list = itertools.combinations(range(1,5),3)

for ptn in arr_list:
  print(ptn)
#(1, 2, 3) (1, 2, 4) (1, 3, 4) (2, 3, 4) 