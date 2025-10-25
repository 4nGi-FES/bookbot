from stats import get_word_count
from stats import get_letter_frequency
from stats import sort_on
from stats import sorted_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_word_count(text)
    num_char = get_letter_frequency(text)
    sort_char = sorted_characters(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_char:
        print(f"{item["char"]}:",item["num"])
    print("============= END ===============")

main()


