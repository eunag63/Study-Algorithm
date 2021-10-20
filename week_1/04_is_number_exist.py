input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 내가 생각한 코드
    # for i in array:
    #     j = array[i]
    #     if j == number:
    #         return True
    #     else:
    #         return False
    # 답안
    for element in array:
        if number == element:
            return True

    return False


result = is_number_exist(3, input)
print(result)