# 문제 1316번 그룹 단어 체커
# 사용자로부터 입력 받은 단어에 그룹 문자가 있는지 없는지

# 1. 문자 n개를 입력받는다.
# 2. if 문을 이용해 그룹 문자가 아니라면 총합에서 -1를 해준다.
# 3. 총합을 출력해준다.

n = int(input())

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i+1] in word[:i]:
                n -= 1
                break

print(n)