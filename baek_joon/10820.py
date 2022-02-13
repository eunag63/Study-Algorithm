# 10820번 문자열 분석
# 구분하는 것은 어렵지 않았음!
# 대신 무한 입력 받기가 구현하기 힘들었음..


import sys

while True:
  word = sys.stdin.readline().rstrip('\n')
  a, b, c, d = 0,0,0,0

  if not word:
    break

  for i in word:
    if i.islower():
      a += 1
    elif i.isupper():
      b += 1
    elif i.isdigit():
      c += 1
    elif i.isspace():
      d += 1

  sys.stdout.write("{} {} {} {}\n".format(a, b, c, d))