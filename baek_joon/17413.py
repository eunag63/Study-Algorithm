# 17413번 단어 뒤집기 2
# 태그 신경써주는게 어려웠음


stack = ""
result = ""
tag = False

words = input()

for i in words:
  if i == "<":
    tag = True
    result += stack[::-1]
    stack = ""
    result += i
    continue
  elif i == ">":
    tag = False
    result += i
    continue
  elif i == " ":
    result += stack[::-1] + " "
    stack = ""
    continue
  if tag:
    result += i
  else:
    stack += i
print(result+stack[::-1])