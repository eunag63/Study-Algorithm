# 17299번 오등큰수
# 오큰수와 유사

n = int(input())
arr = list(map(int, input().split()))

answer = [-1] * n
count = dict()
stack = [0]

print(arr)

for j in arr:
    try:
        count[j] += 1
    except:
        count[j] = 1

for i in range(n):
    # count.append(arr.count(i+1))

    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        answer[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
    i += 1

print(" ".join(map(str, answer)))