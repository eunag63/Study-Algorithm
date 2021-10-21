finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 이진 탐색
def is_existing_target_number_binary_ejin(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2

    return False


# 순차 탐색
def is_existing_target_number_binary_sunca(target, array):
    for number in array:
        if target == number:
            return True
    return False


result_1 = is_existing_target_number_binary_ejin(finding_target, finding_numbers)
result_2 = is_existing_target_number_binary_sunca(finding_target, finding_numbers)
print(result_1, result_2)
