# Muhammet Furkan Yalcin - 101233944

from T1A1_P1_load_data import book_category_dictionary


def sort_books_title(list_stored: dict)->list:
    """
    Preconditions: book_category_dictionary function must be used in this file to be able to get the whole data and this code returns a list with the book data stored as a dictionary book where the books are sorted alphabetically by the titles.
    
    >>>sort_books_title(book_category_dictionary("google_books_dataset.csv"))
    [{'title': '"Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English"', 'category': ['Comics']}, {'title': '"How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon andSchuster', 'pages': 320, 'language': 'English', 'category': ['Economics']}, {'title': '"Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English"', 'category': ['Business']}, {'title': '"The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollinsUK', 'pages': 544, 'language': 'English"', 'category': ['Fiction']}]

    >>>sort_books_title(book_category_dictionary("google_books_dataset.csv"))
    [{'title':'A Feast for Crows (A Song of Ice and Fire. Book 4)','author':'George R.R. Martin','rating': 4.5,'publisher':'HarperCollins UK','pages': 864,'language':'English','category':'Epic'},{'title':'Boy Erased: A Memoir','author':'Garrard Conley','rating': 4,'publisher':'Penguin','pages':352,'category':'Biography','language':'English'}...]

    
    >>>sort_books_title(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': ['Thrillers']}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English', 'category': ['Mystery']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction', 'Mystery']}]
    """
    
    a = 0
    books = []
    c = []
    for key in list_stored.keys():
        books = list_stored[key]
        for book in books:
            c.append(book)
        
    a = len(c)
    for i in range(a-1):
        for j in range(a-1):
            if c[j]['title'] > c[j+1]['title']:
                c[j], c[j+1]  = c[j+1], c[j]
                        
    return c


print('The sorted books are found as in order:',sort_books_title(book_category_dictionary("google_books_dataset.csv")))

    
    