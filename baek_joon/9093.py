# 9093 단어 뒤집기
# 공백일 때와 공백이 아닐 때를 잘 세워 구현하기
# 입력받은 문자의 마지막에 공백을 추가하지 않으면 stack 리스트에서 꺼낼 수 없음!
# 단어가 전부 나오면 Print문의 end 값을 띄어쓰기로 설정하여 단어와 단어 구분해줌

import sys

n = int(input())

stack = []

for i in range(n):

  words = input()
  words += " "

  for k in words:
    # 공백이 아닐 경우
    if k != " ":
      stack.append(k)

    # 공백일 경우
    else:
      while stack:
        print(stack.pop(), end='')
      print(' ', end='')