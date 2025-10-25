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
        