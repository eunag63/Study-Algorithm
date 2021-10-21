n = int(input())


def top(num, first, second, third):
    if num == 1:
        print(first, third)
    else:
        # n-1개의 원판을 2번 탑에 옮기고
        top(num - 1, first, third, second)
        # 맨 아래 원판을 3번 탑으로 옮기고
        print(first, third)
        # 다시 n-1개의 원판을 3번 탑으로 옮긴다.
        top(num - 1, second, first, third)


sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1

print(sum)

top(n, 1, 2, 3)
