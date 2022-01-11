# 9012번 괄호
# 스택 활용

n = int(input())

for i in range(n):
    vps = list(input())
    stack = []
    nothing = False

    for j in range(len(vps)):
        # vps[j]가 '('인 경우
        if vps[j] == '(':
            stack.append(vps[j])
        # vps[j]가 ')'인 경우
        else:
            if not stack:  # 스택이 비어져 있다면
                nothing = True
                break
            else:  # 스택이 안비어져 있다면
                stack.pop()

    if not stack and not nothing:
        print('YES')
    else:
        print('NO')