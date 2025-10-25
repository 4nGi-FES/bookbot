from stats import get_word_count
from stats import get_letter_frequency

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_word_count(text)
    num_char = get_letter_frequency(text)
    return print(f"Found {num_words} total words"), print(num_char)

main()


