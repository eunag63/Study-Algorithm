n = int(input())

stack = []
result = []
count = 1
message = True

for i in range(n):
    num = int(input())
    # push
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    # pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        message = False

if message == False:
    print('NO')
else:
    for i in result:
        print(i)