input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 첫번째 방법
    # for num in array:
    #     for compare_num in array:
    #         if num < compare_num:
    #             break
    #     else:
    #         return num

    # 두번째 방법
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num



result = find_max_num(input)
print(result)