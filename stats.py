def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_letter_frequency(text):
    text = text.lower()
    char_list = list(text)
    char_dict = {}
    for character in char_list:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_characters(num_char):
    char_dict = num_char
    char_list = list(char_dict)
    alpha_list = []
    for char in char_list:
        if char.isalpha() == True:
            alpha_list.append(char)
    data_list = []
    for char in alpha_list:
        val = char_dict[char]
        data_pair = {"char": char, "num": val}
        data_list.append(data_pair)
    data_list.sort(reverse=True, key=sort_on)
    return data_list

