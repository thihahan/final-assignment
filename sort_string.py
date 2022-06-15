# create alphabet dictionary to compare with alphabets
alphabet = {'': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


# which string is smaller than another string as a alphabet order
# example "Aung" < "Benjamin" << "carlo" << "david"

def sort_string(string_one, string_two):
    # change string to list
    # so make it easy to compare each letter
    string_one_list = list(string_one.lower())
    string_two_list = list(string_two.lower())
    index = min(len(string_one_list), len(string_two_list))
    name = compare_string(string_one_list, string_two_list, 0, index-1)
    if name == 0:
        return len(string_one_list) == len(string_two_list)
    if name == string_one_list:
        return "first"
    else:
        return "second"


def compare_string(first, second, index, final):
    if index == final:
        return 0
    if alphabet[first[index]] < alphabet[second[index]]:
        return first
    if alphabet[first[index]] > alphabet[second[index]]:
        return second
    return compare_string(first, second, index+1, final)

