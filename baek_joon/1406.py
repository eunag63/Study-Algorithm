# 1406번 에디터
# 경이로운 스택 사용
# 왜 난 이렇게 생각 못 했지? ㅋ
# 둘로 나눠서 마지막에 합친다..? 이건 천재

from sys import stdin

words = list(stdin.readline().strip())
stack = []

n = int(input())

for j in range(n):
    cmd = stdin.readline()

    # 커서 왼쪽에 문자 추가
    if cmd[0] == "P":
        words.append(cmd[2])

    # 커서 왼쪽으로 움직이기
    elif cmd[0] == "L":
        if words:
            stack.append(words.pop())

    # 커서 오른쪽으로 움직이기
    elif cmd[0] == "D":
        if stack:
            words.append(stack.pop())

    # 커서 왼쪽에 있는 문자 삭제
    elif cmd[0] == "B":
        if words:
            words.pop()

print("".join(words + list(reversed(stack))))