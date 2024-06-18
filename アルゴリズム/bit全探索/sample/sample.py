# bit全探索
import itertools

# ➀順列 重複あり 2**3通り bit全探索
arr_list = itertools.product((0,1), repeat=3)
for ptn in arr_list:
  print(ptn)
#(0, 0, 0) (0, 0, 1) (0, 1, 0) (0, 1, 1) 
#(1, 0, 0) (1, 0, 1) (1, 1, 0) (1, 1, 1)