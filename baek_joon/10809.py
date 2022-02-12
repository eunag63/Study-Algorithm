# 10809번 알파벳 찾기
# 매우 쉬움
# find 함수 좋아요

words = input()
alph = "abcdefghijklmnopqrstuvwxyz"
number = [0] * 26

for i in alph:
  findNum = words.find(i)
  number[ord(i)-97] = findNum

print(*number)