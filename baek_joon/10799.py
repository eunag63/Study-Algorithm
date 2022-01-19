# 10799번 쇠막대기
# 문제이해하는 어려웠던 문제
# 스택 사용하면 ok
# ))이 부분은 생각하지 못함


bar = list(input())

answer = 0
stack = []

for i in range(len(bar)):
  # i가 "("인 경우
  if bar[i] == "(":
    stack.append(bar[i])
  # i가 ")"인 경우
  else:
    # "()"라면 레이저 파트
    if bar[i-1] == "(":
      stack.pop()
      answer+= len(stack)
    # "))"라면 쇠막대기 끄트머리 표현
    else:
      stack.pop()
      answer += 1

print(answer)