# 10866번 덱
# 처음으로 '덱'이라는 자료구조를 알았다
# 신기방기
# 파이썬에서 제공해주는 모듈이 있어서 쉽게 구현~

from collections import deque
import sys

n = int(sys.stdin.readline())

d = deque()

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push_front":
        d.appendleft(order[1])

    elif order[0] == "push_back":
        d.append(order[1])

    elif order[0] == "pop_front":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())

    elif order[0] == "pop_back":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif order[0] == "size":
        print(len(d))

    elif order[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])

    elif order[0] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])