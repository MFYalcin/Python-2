# Muhammet Furkan Yalcin - 101233944
# Soliman Elkhouli - 101244211
# Tsu Chen - 101238818



from T1A1_P1_load_data import book_category_dictionary
from T1A1_check_equal import check_equal





def refactoring(data:list)->list:
    '''
    Returns a list that organizes the rest of the functions and delivers them as clearly as possible.
    >>>refactoring()
    (Function 1)Testing sort_books_title(book_category_dictionary('google_books_dataset.csv')) -- PASSED
    (Function 2)Testing sort_books_author(book_category_dictionary('google_books_dataset.csv')) -- PASSED
    (Function 3)Testing sort_books_publisher(book_category_dictionary('google_books_dataset.csv')) -- PASSED
    (Function 4)Testing sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv')) -- PASSED
    '''
    data = [(check_equal("(Function 1)Testing sort_books_title(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)),(check_equal("(Function 2)Testing sort_books_author(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)),(check_equal("(Function 3)Testing sort_books_publisher(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)),(check_equal("(Function 4)Testing sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv')) --",expected,actual))]
    
    for i in data:
        print(i)
        
        
# So, here the team leader is dealt with the first and last function which are sort_books_title, sort_books_ascending_rate and test functions are also added to do automated testing via check_equal function e

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


   

#Function 1
#Main Script
'''
#print("\n")
#print("Function 1","\n")

total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = sort_books_title(book_category_dictionary('google_books_dataset.csv'))
expected =  [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English\n', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English\n', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English\n', 'rating': '', 'publisher': 'AMACOM', 'pages': 112}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224}, {'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'language': 'English\n', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English\n', 'rating': '', 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English\n', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English\n', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English\n', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English\n', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624}, {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Vintage', 'pages': 32}]


check_equal("(Function 1)Testing sort_books_title(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)
if actual==expected:
    test_pass+=1
else:
    test_failed+=1

'''

    
# Here is Soliman Elkhouli who is last member of team that dealt with the third function which is sort_books_author and his automated testing is added after his main script is done via check_equal function
    
    

def sort_books_author(list_author: dict)->list:
    """
    Preconditions: list_author has to be a list that is produced by the function in case 1 and rearranged by the refactoring function
    returns a list with the book data stored as a dictionary book where the books are sorted alphabetically by author name
    
    >>> sort_books_author(book_category_dictionary("google_books_dataset.csv"))
    [{'title': '"Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English"', 'category': ['Comics']}, {'title': '"How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon andSchuster', 'pages': 320, 'language': 'English"', 'category': ['Economics']}, {'title': '"The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollinsUK', 'pages': 544, 'language': 'English"', 'category': ['Fiction']}, {'title': '"Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English"', 'category': ['Business']}]

    >>> sort_books_author(book_category_dictionary("google_books_dataset.csv"))
    [{'title': '"Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English"', 'category': ['Fiction']}, {'title': '"Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English"', 'category': ['Fiction']}, {'title': '"Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English"', 'category': ['Economics']}, {'title': '"The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'language': 'English"', 'category': ['Fiction']}]
    
    >>> sort_books_author(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': ['Fiction', 'Mystery']}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English', 'category': ['Mystery']}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': ['Thrillers']}]
    """

    '''
    list_books=[]
    sl=[]
    for key in d.keys():
        list_books=d[key]
        for book in list_books:
            book['category'] = key 
            sl.append(book) #adding the publisher into the list sl
        s=len(sl)
        for run in range(s-1):
            for i in range(s-1):
                if sl[i]['publisher']>sl[i+1]['publisher']:
                    sl[i],sl[i+1]=sl[i+1],sl[i]
                if sl[i]['publisher']==sl[i+1]['publisher'] and sl[i].get('title')>sl[i+1].get('title'):
                    sl[i],sl[i+1]=sl[i+1],sl[i]
               
    return sl  
    '''
    t = 0
    author = []
    r = []
    for key in list_author.keys():
        books = list_author[key]
        for book in books:
            book['author'] = key
            r.append(book)
        
    t = len(r)
    for i in range(t-1):
        for j in range(t-1):
            if r[j]['author'] > r[j+1]['author']:
                r[j], r[j+1]  = r[j+1], r[j]
            if r[j]['author'] == r[j+1]['author'] and r[j].get('title')>r[j+1].get('title'):
                r[j], r[j+1]  = r[j+1], r[j]
                        
    return r

#Function 2
#Main Script
'''
#print("\n")
#print("Function 2","\n")

total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = sort_books_author(book_category_dictionary('google_books_dataset.csv'))
expected =  [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Adventure', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Boy Erased: A Memoir', 'author': 'Biography', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'Business', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Classics', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Comics', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Bring Me Back', 'author': 'Crime', 'language': 'English\n', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Detective', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'How To Win Friends and Influence People', 'author': 'Economics', 'language': 'English\n', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'Epic', 'language': 'English\n', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Fantasy', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Fiction', 'language': 'English\n', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Finance', 'language': 'English\n', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'The Mysterious Affair at Styles', 'author': 'Horror', 'language': 'English\n', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Humor', 'language': 'English\n', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Information Technology', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'Legal', 'language': 'English\n', 'rating': '', 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Management', 'language': 'English\n', 'rating': '', 'publisher': 'AMACOM', 'pages': 112}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Money Management', 'language': 'English\n', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'Total Control', 'author': 'Mystery', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Mythical Creatures', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'How To Win Friends and Influence People', 'author': 'Psychology', 'language': 'English\n', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'We Should All Be Feminists', 'author': 'Social Science', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Vintage', 'pages': 32}, {'title': 'Spider-Man: Anti-Venom', 'author': 'Superheroes', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Thrillers', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Traditional', 'language': 'English\n', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40}]



check_equal("(Function 2)Testing sort_books_author(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)
if actual==expected:
    test_pass+=1
else:
    test_failed+=1
'''


# Fellow teammate Tsu Chen is responsible for sort_books_publisher. His automated testing is added below his main script via check_equal function.

def sort_books_publisher(d:dict)->list:
    """
    Returns a list of dictionaries that have been sorted by the publisher and title (if publishers are the same). 
    
    >>>sort_books_publisher(data)
    {'title': 'Management (The Brian Tracy Success Library)', 
    'author': 'Brian Tracy', 
    'language': 'English\n', 
    'rating': '', 'publisher': 
    'AMACOM', 
    'pages': 112, 
    'category': 'Management'}
    """
    list_books=[]
    sl=[]
    for key in d.keys():
        list_books=d[key]
        for book in list_books:
            book['category'] = key 
            sl.append(book) #adding the publisher into the list sl
        s=len(sl)
        for run in range(s-1):
            for i in range(s-1):
                if sl[i]['publisher']>sl[i+1]['publisher']:
                    sl[i],sl[i+1]=sl[i+1],sl[i]
                if sl[i]['publisher']==sl[i+1]['publisher'] and sl[i].get('title')>sl[i+1].get('title'):
                    sl[i],sl[i+1]=sl[i+1],sl[i]
               
    return sl  

#Main Script
#Function  3
'''
#print("\n")
#print("Function 3","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = sort_books_publisher(book_category_dictionary('google_books_dataset.csv'))
expected = [{'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English\n', 'rating': '', 'publisher': 'AMACOM', 'pages': 112, 'category': 'Management'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': 'Information Technology'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Adventure'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Mythical Creatures'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'language': 'English\n', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': 'Humor'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English\n', 'rating': '', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Legal'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Fantasy'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English\n', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Finance'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English\n', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Money Management'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Thrillers'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'category': 'Business'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English\n', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Epic'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English\n', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Crime'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English\n', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Horror'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English\n', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Traditional'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics'}, {'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Superheroes'}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Mystery'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'language': 'English\n', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'category': 'Biography'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Economics'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Psychology'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Detective'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Classics'}, {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Vintage', 'pages': 32, 'category': 'Social Science'}]

check_equal("(Function 3)Testing sort_books_publisher(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)
if actual==expected:
    test_pass+=1
else:
    test_failed+=1
'''    
    
    
    
def sort_books_ascending_rate(dict_stored:dict)->list:
    """
    Preconditions: book_category_dictionary function must be used in this file to be able to get the whole data and this code returns a list with the book data stored as a dictionary book where the books are sorted starting with N/A in order by ascending rating.
    
    >>>sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': '"Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English"', 'category': 'Comics'}, {'title': '"How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon andSchuster', 'pages': 320, 'language': 'English', 'category': 'Economics'}]

    >>>sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title':'Boy Erased: A Memoir','author':'Garrard Conley','rating': 4,'publisher':'Penguin','pages':352,'category':'Biography','language':'English'},{'title':'A Feast for Crows (A Song of Ice and Fire. Book 4)','author':'George R.R. Martin','rating': 4.5,'publisher':'HarperCollins UK','pages': 864,'language':'English','category':'Epic'}]

    
    >>>sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': 'Thrillers'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English', 'category': 'Mystery'}]
    """    
 
    
    d = 0
    books = []
    l = []
    for key in dict_stored.keys():
        books = dict_stored[key]
        for book in books:
            book['rating'] = key
            l.append(book)
        
            
        
    d = len(l)
    for i in range(d-1):
        for j in range(d-1):
            if l[j]['rating'] > l[j+1]['rating']:
                l[j], l[j+1]  = l[j+1], l[j]
            if l[j]['rating'] == 'N/A':
                l[j], l[j+1]  = l[j+1], l[j]
            if l[j]['rating']==l[j+1]['rating'] and l[j].get('rating')>l[j+1].get('rating'):
                    l[j],l[j+1]=l[j+1],l[j]            
                        
            
                
    return l





#Function 4
#Main Script
'''
#print("\n")
#print("Function 4","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv'))
expected = [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 'Adventure', 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'language': 'English\n', 'rating': 'Biography', 'publisher': 'Penguin', 'pages': 352}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English\n', 'rating': 'Business', 'publisher': 'Harper Collins', 'pages': 224}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English\n', 'rating': 'Classics', 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating': 'Comics', 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English\n', 'rating': 'Crime', 'publisher': 'HarperCollins UK', 'pages': 368}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English\n', 'rating': 'Detective', 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating': 'Economics', 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English\n', 'rating': 'Epic', 'publisher': 'HarperCollins UK', 'pages': 864}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 'Fantasy', 'publisher': 'Hachette UK', 'pages': 96}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating': 'Fiction', 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English\n', 'rating': 'Finance', 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English\n', 'rating': 'Horror', 'publisher': 'HarperCollins UK', 'pages': 208}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'language': 'English\n', 'rating': 'Humor', 'publisher': 'Hachette UK', 'pages': 336}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': 'English\n', 'rating': 'Information Technology', 'publisher': 'Crown Business', 'pages': 464}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English\n', 'rating': 'Legal', 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English\n', 'rating': 'Management', 'publisher': 'AMACOM', 'pages': 112}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English\n', 'rating': 'Money Management', 'publisher': 'Hachette UK', 'pages': 30}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English\n', 'rating': 'Mystery', 'publisher': 'Pan Macmillan', 'pages': 624}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 'Mythical Creatures', 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating': 'Psychology', 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': 'English\n', 'rating': 'Social Science', 'publisher': 'Vintage', 'pages': 32}, {'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'language': 'English\n', 'rating': 'Superheroes', 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English\n', 'rating': 'Thrillers', 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English\n', 'rating': 'Traditional', 'publisher': 'HarperCollins UK', 'pages': 40}]


check_equal("(Function 4)Testing sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv')) --",expected,actual)
if actual==expected:
    test_pass+=1
else:
    test_failed+=1
    
'''





