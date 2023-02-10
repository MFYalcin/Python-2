# Muhammet Furkan Yalcin - 101233944
# Soliman Elkhouli - 101244211
# Tsu Chen - 101238818

import string


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
    categories = set()
    lst = []
    for line in infile:
        word_list = line.strip(string.punctuation).split(",")
        categories.add(word_list[5])
        
        rating = word_list[2]
        if rating != "N/A" and rating!= "rating":
            rating = float(rating)
        else:
            rating = ""
        
        pages = word_list[4]
        if pages != "pages":
            pages = int(pages)
        else:
            pages = ""
        lst.append({"title": word_list[0],"author":word_list[1],"language":word_list[6],"rating": rating, "publisher": word_list[3],"pages":pages})

        for book in line:
            if word_list[5] not in book_dictionary:
                category = word_list[5]  
                book_dictionary[category] = lst
            lst= []
        
    book_dictionary.pop(category)
    return book_dictionary


filename = 'google_books_dataset.csv'
word_list = book_category_dictionary(filename)
print('File', filename, 'contains', len(word_list), 'distinct words')
print('The book categories in this file is:', word_list)




