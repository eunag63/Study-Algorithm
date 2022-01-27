# 1935번 후위표기식 2
# 스택을 이용하면 잘 풀림

num = int(input())
text = input()
stack = []
alpha = [0]*num

for i in range(num):
  alpha[i] = int(input())

for j in text:
  if j.isalpha():
    stack.append(alpha[ord(j) - ord('A')])
  else:
      str2 = stack.pop()
      str1 = stack.pop()

      if j == "+":
        stack.append(str1 + str2)
      elif j == "-":
        stack.append(str1 - str2)
      elif j == "*":
        stack.append(str1 * str2)
      elif j == "/":
        stack.append(str1 / str2)

print(format(stack[0], ".2f"))