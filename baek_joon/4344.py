c = int(input())

for _ in range(c):
  array = list(map(int, input().split()))

  #점수 평균 구하기
  student = array[0]
  score = sum(array[1:])
  average = score / student

  #평균 이상 학생 비율 구하기
  count = 0
  for i in array[1:]:
    if i > average:
      count += 1
  rate = count/student * 100

  #소수점
  print("{:.3f}%".format(rate))