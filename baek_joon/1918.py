# 1918번 후위 표기식
# 스택 이용!
# 30분 안에 풀기 실패 ㅠ

text = input()
answer = ''
stack = []

for t in text :
    if t.isalpha() :
        answer += t
    else :
        if t == '(' :
            stack.append(t)
        elif t == '*' or t == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                answer += stack.pop()
            stack.append(t)
        elif t == '+' or t == '-' :
            while stack and stack[-1] != '(' :
                answer += stack.pop()
            stack.append(t)
        elif t == ')' :
            while stack and stack[-1] != '(' :
                answer += stack.pop()
            stack.pop()

while stack :
    answer += stack.pop()

print(answer)