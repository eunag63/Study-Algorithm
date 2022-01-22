# 17298번 오큰수
# 문제이해가 어려웠음
# 스택으로 풀어야 하는건 알았지만 '어떻게' 스택으로 풀지 막막
# push와 pop을 이용해서 비교, 교체 가능하다는 걸 알았음

import sys

i = int(input())

arr = list(map(int, sys.stdin.readline().split()))

answer = [-1] * i # 오큰수가 없을 경우 -1 출력
stack = []

stack.append(0)
for i in range(i):
  while stack and arr[stack[-1]] < arr[i]:
    answer[stack.pop()] = arr[i]
  stack.append(i)

print(*answer)