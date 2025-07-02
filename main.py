from stats import num_words_func
from stats import num_char_func

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_char = num_char_func(book_text)
    num_words = num_words_func(book_text)


    return print(f"{num_words} words found in the document"),print(num_char)

main()
     


