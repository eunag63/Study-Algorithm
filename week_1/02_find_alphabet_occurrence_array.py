input = "hello my name is sparta"


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!

    for i in string:
        if not i.isalpha():
            continue
        j = ord(i) - ord("a")
        alphabet_occurrence_array[j] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))