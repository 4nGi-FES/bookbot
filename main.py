def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_word_count(text)
    return print(f"Found {num_words} total words")

main()