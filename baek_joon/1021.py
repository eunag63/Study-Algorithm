from collections import deque

n, m = map(int,input().split())
pick = list(map(int,input().split()))

queue = deque([i for i in range(1, n+1)])
count = 0


while pick:
    # 1번 연산
    if queue[0] == pick[0]:
        queue.popleft()
        del pick[0]
    else:
      # 왼쪽으로 이동할 지 오른쪽으로 이동할 지를 결정
        # 2번 연산
        if queue.index(pick[0]) > len(queue) / 2:
            while queue[0] != pick[0]:
                queue.appendleft(queue.pop())
                count += 1
        # 3번 연산
        else:
            while queue[0] != pick[0]:
                queue.append(queue.popleft())
                count += 1

print(count)