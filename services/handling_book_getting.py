import re
import os

BOOK_PATH = os.path.join(os.getcwd(), 'books/Bulgakov.txt')
page_size = 1050
book: dict[int, str] = {}

pattern = '[^\w\s]+'
def _get_part_text(text: str, start, page_size):
    result = re.finditer(pattern, text[start:])
    for i in result:
        if i.end() > page_size:
            break
        result = i.end()
    return text[start:result+start], result

def prepare_book(path: str):
    with open(path) as file:
        books = file.read()
        count_page, start = 1, 0
        generate_page = _get_part_text(books, start, page_size)
        book.setdefault(count_page, generate_page[0])
        while len(books) - start > page_size:
            count_page, start = count_page + 1, start + generate_page[1]
            generate_page = _get_part_text(books, start, page_size)
            book.setdefault(count_page, generate_page[0].lstrip())

prepare_book(BOOK_PATH)

