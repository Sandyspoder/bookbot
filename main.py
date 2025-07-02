from stats import num_words_func, num_char_func, sort_char_dict
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_char = num_char_func(book_text)
    sorted_num_char = sort_char_dict(num_char)
    num_words = num_words_func(book_text)


    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for i in range(0,len(sorted_num_char)):
        print(f"{sorted_num_char[i]["char"]}: {sorted_num_char[i]["num"]}")
    print(f"============= END ===============")
main()
     


