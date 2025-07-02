def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()

    return book_text

def main():
    print(get_book_text("books/frankenstein.txt"))


main()
     


