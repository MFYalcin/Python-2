# Muhammet Furkan Yalcin - 101233944


import string

def test_float(desc:str, expected:float, actual:float)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_float('Testing 1.1',21.4,21.3)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_float('Testing 1.2',40.5,40.2)
    Test failed
    0
    >>>test_float('Testing 1.3',20.4,20.4)
    Test passed
    1
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0 


def test_int(desc:str, expected:int, actual:int)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_int('Testing 1.1',21,22)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_int('Testing 1.2',40,68)
    Test failed
    0
    >>>test_int('Testing 1.3',20,20)
    Test passed
    1
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0 

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
        lst.append({"title ": word_list[0],"author":word_list[1],"language":word_list[6],"rating ": rating, "publisher ": word_list[3],"pages ":pages})

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



