# 처음 풀었을 때
sum = 0

for i in range(len(absolutes)):
  if signs[i] == "true":
    absolutes[i] = +(absolutes[i])
  elif signs[i] == "false":
    absolutes[i] = -(absolutes[i])

  sum += absolutes[i]
print(sum)

# 테스트 끝나고 정리
sum = 0

for i in range(len(absolutes)):
  if signs[i] == "true":
    sum += absolutes[i]
  elif signs[i] == "false":
    sum -= absolutes[i]

print(sum)