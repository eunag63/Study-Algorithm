# 1157 요세푸스
# 한 바퀴 돌았을 때가 주요 포인트

n, k = map(int, input().split())
array = [i for i in range(1, n+1)] # 1~n번째까지의 배열 생성

kill = []
num = 0

for j in range(n):
  num += k-1

  # 한바퀴 돌았을 때
  if num >= len(array):
    num = num%len(array)

  kill.append(str(array.pop(num)))

print("<",", ".join(kill)[:],">", sep='')