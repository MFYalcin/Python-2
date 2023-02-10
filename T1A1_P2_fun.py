# Muhammet Furkan Yalcin - 101233944

from T1A1_P1_load_data import book_category_dictionary
import string

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

val_tpl = ('title','author', 'language', 'publisher', 'category', 'rating','pages')
a = dict()
b = add_book(a,(val_tpl))

    

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





def get_books_by_category(dict_std: dict,ctg_prt: str)->int:
    '''
    Precondition: csv or txt file must be used during the project and title and author of the book are ordered in the shell
    Returns a new dictionary that is contained title and author of the books
    >>>get_books_by_category(dict_std,ctg_prt):
    The category 'Fiction' has 38 books. This is the list of books:
    Book 1: "Antiques Roadkill: A Trash 'n' Treasures Mystery" by "Barbara Allan"
    Book 2: "The Painted Man (The Demon Cycle. Book 1)" by "Peter V. Brett"
    '''
    lst = dict_std.get(ctg_prt)
    num = len(lst)
    print("The category", ctg_prt, "has", num, "books. This is the list of books:")
    a = 0
    for i in lst:
        singlebook = dict_std
        title = singlebook.get('title')
        author = singlebook.get('author')
        a += 1
        print("Book", a, ":", title, "by", author)
        return a
 










