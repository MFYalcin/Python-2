# Student name: Royce Chen, Student number: 101238818




import string
from typing import List

def book_category_dictionary(filename: str) -> dict[str:list[dict]]:
    """Return a dictionary of all the distinct words in the specified file,
    sorted in ascending order and first item in the dictionary needs to be categories in the file.  
    Precondition: Specified ile must be in a format of csv or txt in order for it be worked.
    
    >>> word_list = book_category_dictionary('google_books_dataset.csv')
    >>> {"Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery","author": " Barbara Allan","language ": "English","rating": 3.3, ["title": "The Painted Man (The Demon Cycle. Book 1)", "author":"Peter V. Brett", "language":"English","rating": 4.5]...}
    >>> len(word_list) 
    25
    """
    infile = open(filename)
    book_dictionary= dict()
    lst = []
    infile.readline()
    
    for line in infile:
        word_list = line.strip(string.punctuation).split(",")
        category = word_list[5]
        
        rating = word_list[2]
        if rating != "N/A":
            rating = float(rating)
        else:
            rating = ""
        
        book = {"title": word_list[0], "author": word_list[1], "language": word_list[6], "rating": rating, "publisher": word_list[3], "pages": word_list[4]}
        if book not in lst:
            lst.append(book)
            if not book_dictionary.get(category):
                book_dictionary[category] = [book]
            else:
                book_dictionary[category].append(book)

    return book_dictionary


#testing
"""
if __name__ == '__main__':
    all_books = list(book_category_dictionary('google_books_dataset.csv').values())
    books = [str(book) for book_list in all_books for book in book_list]
    print(len(books), len(list(set(books))))
"""
