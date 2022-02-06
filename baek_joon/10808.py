# 10808번 알파벳 개수
# 진짜 쉬운 문제인데 아스키 코드를 이용할 생각을 못했다 ㅠㅠㅠ

alphabet = input()

number = [0 for i in range(26)]

for i in alphabet:
  number[ord(i) - 97] += 1

print(*number)