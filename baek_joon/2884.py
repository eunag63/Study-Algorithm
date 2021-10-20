# h, m = map(int, input().split())
#
# m = m - 45
#
# if m < 0:
#   h -= 1
#   m += 60
#
# if h < 0:
#   h += 24
#
# print(h, m)

# 두번째
h, m = map(int, input().split())

if m >= 45:
  print(h, m-45)
elif h > 0 and m < 45:
  print(h-1, m+15)
else:
  print(23, m+15)