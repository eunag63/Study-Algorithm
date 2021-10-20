input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 첫번째
    # alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z",]
    #
    # max_occurrence = 0
    # max_alphabet = alphabet_array[0]
    #
    # for alphabet in alphabet_array:
    #     occurence = 0
    #     for char in string:
    #         if char == alphabet:
    #             occurence += 1
    #     if occurence > max_occurrence:
    #         max_occurrence = occurence
    #         max_alphabet = alphabet
    #
    # return max_alphabet

    # 두번째
    # alphabet_occurrence_array = [0] * 26
    #
    # for i in string:
    #     if not i.isalpha():
    #         continue
    #     j = ord(i) - ord("a")
    #     alphabet_occurrence_array[j] += 1
    #
    # max_occurrence = 0
    # max_alphabet_index = 0
    # for index in range(len(alphabet_occurrence_array)):
    #     alphabet_occurrence = alphabet_occurrence_array[j]
    #     if alphabet_occurrence > max_occurrence:
    #         max_alphabet_index = index
    #         max_occurrence = alphabet_occurrence
    #
    # return chr(max_alphabet_index + ord("a"))


    # 세번째
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if not i.isalpha():
            continue
        j = ord(i) - ord("a")
        alphabet_occurrence_array[j] += 1

    max_num = alphabet_occurrence_array[0]
    for num in alphabet_occurrence_array:
        if num < max_num:
            max_num = num
    return chr(max_num + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)