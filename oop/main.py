from book_class import Book

def main():
    # 1. This triggers __init__
    my_book = Book("1984", "George Orwell", 1949)

    # 2. This triggers __str__
    print(my_book)  

    # 3. This triggers __repr__
    print(repr(my_book))  

    # 4. This triggers __del__
    del my_book

if __name__ == "__main__":
    main()