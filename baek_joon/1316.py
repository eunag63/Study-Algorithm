# 1. 단어 n개를 입력받는다.
# 2. if 문을 이용해 그룹 단어가 아니라면 총합에서 -1를 해줍니다.
# 3. 총합을 출력해줍니다.

n = int(input())

for _ in range(n):
    word = input()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i+1] in word[:i]:
                n -= 1
                break

print(n)