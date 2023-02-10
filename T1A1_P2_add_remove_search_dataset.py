# Muhammet Furkan Yalcin - 101233944
# Soliman Elkhouli - 101244211
# Tsu Chen - 101238818



from T1A1_P1_load_data import book_category_dictionary
import string

# So, here the team leader is dealt with the first three function which are add_book , remove_book and get_books_by_category and test functions are also added to do automatic testing.

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description,outcome, str(outcome_type).strip('<class> '), expected, str(expected_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description,outcome,expected))
    else:
        print("{0} PASSED".format(description))
    print("------")
    
    
def main():
    if __T1A1_P1_load_data__ != '__main__':
        main()

def test_str(desc:str, expected:str, actual:str)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_int('Testing 1.1',21,22)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_int('Testing 1.2','40','68')
    Test failed
    0
    >>>test_int('Testing 1.3','20','20')
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
    
  
def test_dict(desc:str, expected:dict, actual:dict)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_dict('Testing 1.1', {'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288}]}, {'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288.0}]})
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_dict('Testing 1.2', {'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288}]},{'Comics': [{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96}]})
    Test failed
    0
    >>>test_dict('Testing 1.3', {'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288}]}, {'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288}]})
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
    


    
#Function 1
def add_book(dict_add:dict,val_tpl:tuple)->dict:
    '''
    Precondition: csv or txt file must be used during the project and added books must be certified whether they are added or not.
    Returns a dictionary that the books that are added to first empty dictionary argument by the tuples of values such as title,author,rating,publisher,page,category,language,
    >>>add_book(dict(),('title','author','rating','publisher','pages','category','language')):
    {'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96....}
    '''    
    a = val_tpl[0]    
    val_tpl = list(val_tpl)
    del val_tpl[0]    
    val_tpl = tuple(val_tpl)
    if a in dict_add:
        dict_add[a].append(val_tpl)
    else:
        dict_add[a] = [val_tpl]
    check = 0
    
    if a in dict_add:
        if a in dict_add[a]:
            check = 1
    
    if check==0:
        return("The book has been added correctly")
    else:
        return("There was an error adding the book")
        
    return dict_add

a = dict()
b = add_book(a,('title','author', 'language', 'publisher', 'category', 'rating','pages'))

    
# Function 2
def remove_book(dict_rmv:dict,title_book,ctg)->dict:
    '''
    Precondition: csv or txt file must be used during the project
    Returns a new dictionary that is removed by the second and third arguments that are titles and categories of the file.
    >>>remove_book(dict_rmv,title,book_ctg)
    {'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},
    '''
    check2 = 0
    if ctg in dict_rmv:
        for i in dict_rmv[ctg]:
            if title_book in i[0]:
                dict_rmv[ctg].remove(i)
                check2 = 1
    if check2 == 1:
        return ("There was an error removing the book. Book not found.")
    else:
        return ("The book has been removed correctly")
    return dict_rmv



#Function 3
def get_books_by_category(dict_std: dict,ctg_prt: str)->int:
    '''
    Precondition: csv or txt file must be used during the project and title and author of the book are ordered in the shell
    Returns a new dictionary that is contained title and author of the books
    >>>get_books_by_category(dict_std,ctg_prt):
    The category 'Fiction' has 38 books. This is the list of books:
    Book 1: "Antiques Roadkill: A Trash 'n' Treasures Mystery" by "Barbara Allan"
    Book 2: "The Painted Man (The Demon Cycle. Book 1)" by "Peter V. Brett"
    '''
    lst = dict_std.get('category')
    num = len(lst)
    print("The category", ctg_prt, "has", num, "books. This is the list of books:")
    a = 0
    for i in lst:
        singlebook = dict_std
        title = singlebook.get("title")
        author = singlebook.get("author")
        a += 1
        print("Book", a, ":", title, "by", author)
        print('...')
        return a
 


'''
#Automatic Testing
add1 = add_book({'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},('title','author','rating','publisher','pages','category','language'))
add2 = add_book({'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},('title','author','rating','publisher','pages','category','language'))
add3 = add_book({'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},('title','author','rating','publisher','pages','category','language'))

print('Exercise 1.1: ',add1)
print('Exercise 1.2: ',add2)
print('Exercise 1.3: ',add3)


t1_1 = test_dict('Testing 1.1',{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288})
                  
t1_2 = test_dict('Testing 1.2',{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96})
t1_3 = test_dict('Testing 1.3',{'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},{'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320})

print('Testing 1.1: ',t1_1)
print('Testing 1.2: ',t1_2)
print('Testing 1.3: ',t1_3)


rmv1 = remove_book({'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},'title','author')
rmv2 = remove_book({'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},'title','author')
rmv3 = remove_book({'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},'title','author')

print('Exercise 2.1: ',rmv1)
print('Exercise 2.2: ',rmv2)
print('Exercise 2.3: ',rmv3)

t2_1 = test_dict('Testing 2.1',{'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},{'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288})
                  
t2_2 = test_dict('Testing 2.2',{'author': 'Cullen Bunn', 'language': 'English', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},{'author': 'Cullen Bunn', 'language': 'English', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96})
t2_3 = test_dict('Testing 2.3',{'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},{'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320})

print('Testing 3.1: ',t2_1)
print('Testing 3.2: ',t2_2)
print('Testing 3.3: ',t2_3)

ctg1 = get_books_by_category({'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan','category':'Fiction','language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},'Fiction')
ctg2 = get_books_by_category({'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn','category':'Comics', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},'Comics')
ctg3 = get_books_by_category({'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie','category':'Economics', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},'Economics')

print('Exercise 3.1: ',ctg1)
print('Exercise 3.2: ',ctg2)
print('Exercise 3.3: ',ctg3)

t3_1 = test_str('Testing 3.1',"Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan","Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan")
t3_2 = test_str('Testing 3.2',"Book 2: The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett","Book 2: The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett")
t3_3 = test_str('Testing 3.3',"Book 3: Edgedancer: From the Stormlight Archive by Brandon Sanderson","Book 3: Edgedancer: From the Stormlight Archive by Brandon Sanderson")

print('Testing 3.1: ',t3_1)
print('Testing 3.2: ',t3_2)
print('Testing 3.3: ',t3_3)

'''


#Function4

# Fellow teammate Tsu Chen is responsible for get_books_by_rate and get_books_by_title functions. His automatic testing is added below his main script.
def get_books_by_rate(booklist: dict, given_rating: int) -> int:
    """
    Returns the number of books by the given rating that is inputted by the user. 
    >>>get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),4)
    There are 17 books whose rating is between 4 and 5 . This is the list of books: 
    Book 1: "Deadpool Kills the Marvel Universe" by "Cullen Bunn"
    Book 2: "How To Win Friends and Influence People" by "Dale Carnegie"
    Book 3: "Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth" by "T. Harv Eker"
    """
    books_rating = []
    
    for category, books in booklist.items():
        for book in books:
            rating = book.get('rating')
            if rating is not None and rating != '' and rating != 'N/A':
                if float(rating) >= given_rating and float(rating) < (given_rating + 1) and book['title'] not in books_rating:
                    books_rating += [(book['title'], book['author'])]
    print('There are',len(books_rating),'books whose rating is between',given_rating,'and',given_rating + 1,'. This is the list of books: ')
   
    for i in range(len(books_rating)):
        print(f'Book {i+1}: "{books_rating[i][0]}" by "{books_rating[i][1]}"')
    return len(books_rating)



#Function 5
def get_books_by_title(dictionary:dict, title:str) -> bool:
    """
    Returns a string which shows if the book has been found or not, 
    by taking in the dictionary and title inputted by the user.
    >>>get_books_by_title(book_category_dictionary('google_books_dataset.csv'),"Antiques Roadkill: A Trash 'n' Treasures Mystery")
    The book has been found
    """
    found_title = False
    for i in dictionary:
        for j in dictionary[i]:
            if title in j['title']:
                found_title = True
    if found_title == True:
        print("The book has been found")
    else:
        print("The book has NOT been found")
        
    return found_title






    
#Main Script

#Function 4 
'''
print("\n")
print("Function 4","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = get_books_by_rate(book_category_dictionary("google_books_dataset.csv"),3)
expected = 4
check_equal("Testing get_books_by_rate(book_category_dictionary('google_books_dataset.csv'),3) --",expected,actual)
if actual==expected:
    test_pass+=1
else:
    test_failed+=1
    
#Function 5 

print("\n")
print("Function 5","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Roadkill: A Trash 'n' Treasures Mystery")
expected = True
check_equal("Testing get_books_by_title(book_category_dictionary('google_books_dataset.csv'),'Antiques Roadkill: A Trash 'n' Treasures Mystery') --",expected,actual)
total_test+1
if actual==expected:
    test_pass+=1
else:
    test_failed+=1
    
'''

# Here is Soliman Elkhouli who is last member of team that dealt with the last three functions which are  get_books_by_author, get_books_by_publisher and get_all_categories_for_book_title and his automatic testing is added after his main script is done.


# Function 6
def get_books_by_author(google_books_dataset: dict, author: str) -> int:
    """
   Returns the number of books written by a specified author 
   >>> get_books_by_author(book_category_dictionary('google_books_dataset.csv'), Barbara Allana)
   Author Barbara Allan has published these following books:
   book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery: 3.3
    """
    categories = list(google_books_dataset.keys())
    print("Author", author, "has published these following books:")
    n = 0
    books = []
    for x in categories:
        category = x
        lst = google_books_dataset.get(category)
        for x in lst:
            book = x
            title = book.get('title')
            if title not in books:
                books += [title]
                rating = book.get('rating')
                writer = book.get('author')
                if writer == author:
                    print("Book", n, ":", title, "Rate:", rating)
                n += 1
    return n

# Function 7 

def get_books_by_publisher(booklist: dict, publisher: str)->int:
    """
    Returns number of books published by a given publisher 
    
    >>>  get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'), Kensington Publishing Corp.)
    Pubisher Kensington Publishing Corp. has published the following books:
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery, by Barbara Allan
    """
    categories = list(booklist.keys())
    print("Pubisher", publisher, "has published the following books:")
    n = 0
    books = []
    for x in categories:
        category = x
        lst = booklist.get(category)
        for x in lst:
            book = x
            publisher1 = book.get('publisher')
            title = book.get('title')
            if title not in books:
                books += [title]
                author = book.get('author ')
                if publisher1 == publisher:
                    print("Book", n, ":", title, "by", author)
                    n += 1
    return n


# Function 8 


def get_all_categories_for_book_title(booklist: dict, title: str)->int:
    """
    Returns all the categories that are related to a given book
    
    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), Antiques Roadkill: A Trash 'n' Treasures Mystery)
    The book  Antiques Roadkill: A Trash 'n' Treasures Mystery is in the following categories:
    Category 1 : Fiction
    Category 2: Detective
    Category 3: Mystery    
    """
    categories = list(booklist.keys())
    print("The book ", title, "is in the following categories:")
    n = 0
    books = []
    for x in categories:
        category = x
        lst = booklist.get(category)
        for x in lst:
            book = x
            if book.get('title') == title:
                print("Category", n, ":", category)
                n += 1
    return n



# Test 6
'''
print("\n")
print("Function 6","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test += 1
actual = get_books_by_author(book_category_dictionary("google_books_dataset.csv"),"Barbara Allan")
expected = 21
check_equal("Testing get_books_by_author(book_category_dictionary('google_books_dataset.csv'),'Barbara Allan') --",expected,actual)
total_test+1
if actual == expected:
    test_pass += 1
else:
    test_failed += 1


# Test 7 

print("\n")
print("Function 7","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test += 1
actual = get_books_by_publisher(book_category_dictionary("google_books_dataset.csv"),"Kensington Publishing Corp.")
expected = 1
check_equal("Testing get_books_by_publisher(book_category_dictionary('google_books_dataset.csv'),'Kensington Publishing Corp.') --",expected,actual)
total_test+1
if actual == expected:
    test_pass += 1
else:
    test_failed += 1
    
# Test 8 

print("\n")
print("Function 8","\n")
total_test = 0
test_pass = 0
test_failed = 0

total_test+=1
actual = get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Roadkill: A Trash 'n' Treasures Mystery")
expected = 1
check_equal("Testing get_all_categories_for_book_title('google_books_dataset.csv'),'Antiques Roadkill: A Trash 'n' Treasures Mystery') --",expected,actual)
total_test+1
if actual == expected:
    test_pass += 1
else:
    test_failed+=1
 
'''  
    
    
    

