# 10845번 큐
# 스택과 매우 유사하나 pop만 다름 (주의)

import sys

n = int(sys.stdin.readline())

queue = []

for i in range(n):
  order = sys.stdin.readline().split()

  if order[0] == "push":
    queue.append(order[1])

  elif order[0] == "size":
    print(len(queue))

  elif order[0] == "empty":
    if len(queue) == 0:
      print(1)
    else:
      print(0)

  elif order[0] == "pop":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.pop(0))


  elif order[0] == "front":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])


  elif order[0] == "back":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])