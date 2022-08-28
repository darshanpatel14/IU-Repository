# class
# creating new class creates new types of object,
# allowing new instance of that type to be made
# class provide a way to bundle data and functionality together

# using class keyword

class TextBook():

    def print_book_title(self, book_title):
        print(book_title)

# first param of every class method is defined with
# self keyword it always refers to the current instance of the class


def main():

    text_book = TextBook()
    book_title = "Learn Python"

    text_book.print_book_title(book_title)


if __name__ == "__main__":
    main()
