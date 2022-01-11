ranking = [6,6,5,4,3,2,1]
high = 0
low = 0

# 최저 공통 숫자 갯수
for i in win_nums:
  low += lottos.count(i)

# 최고 공통 숫자 갯수
high = lottos.count(0) + low

print(high, low)

# 순위 정하기
answer = [ranking[high], ranking[low]]
print(answer)