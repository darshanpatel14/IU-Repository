# used it for the initialize the object

# this method is defined with the "__init__" reserve in python

def __init__(self):
    ''' Initialize'''


class TextBook():

    def __init__(self, page_number=None):
        if page_number is not None:
            self.page_number = page_number
        else:
            self.page_number = None

    def print_book_title(self, book_title):
        print(book_title)

    def print_book_pages_number(self):
        if self.page_number is not None:
            print("The number of book pages is {}".format(self.page_number))


def main():
    page_number = 300

    text_book = TextBook(page_number)

    text_book.print_book_title("Programming with python")

    text_book.print_book_pages_number()


if __name__ == '__main__':
    main()
