S = input()
num1 = 0
num2 = 0

for i in range(len(S)):
  if S[i].islower():    # islower() 小文字だとTrueを返す
                        # isupper() 大文字だとTrueを返す
    num2 += 1
  else:
    num1 += 1

if num1 < num2:
  print(S.lower())      # Sを小文字で返す
else:
  print(S.upper())      # Sを大文字で返す