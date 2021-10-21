input = "abcba"


# 반복문
def is_palindrome_1(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False

    return True


# 재귀함수
def is_palindrome_2(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome_2(string[1:-1])


print(is_palindrome_1(input))
print(is_palindrome_2(input))
