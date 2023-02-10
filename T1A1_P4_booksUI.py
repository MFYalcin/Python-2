# Muhammet Furkan Yalcin - 101233944
# Soliman Elkhouli - 101244211
# Tsu Chen - 101238818

from T1A1_P1_load_data import book_category_dictionary
from T1A1_P2_add_remove_search_dataset import add_book
from T1A1_P2_add_remove_search_dataset import remove_book
from T1A1_P2_add_remove_search_dataset import get_books_by_category
from T1A1_P2_add_remove_search_dataset import get_books_by_author
from T1A1_P2_add_remove_search_dataset import get_books_by_rate
from T1A1_P2_add_remove_search_dataset import get_books_by_title
from T1A1_P3_sorting_fun import sort_books_title, sort_books_author, sort_books_publisher, sort_books_ascending_rate


from os import system
from pprint import pprint



# So, here the team leader is dealt with the first case which contain add_book and remove_book. Test functions are not included since they are not asked in the milestone.





def UI_add_remove()->None:
    '''
    Prompts the user enter related book parts and make the user whether they want to continue or not at the end.
    >>>Please type your command:
     1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
    T)itle R)ate A)uthor P)ublisher C)ategory
    5- GCT) Get all Categories for book Title
    6- S)ort books
    T)itle R)ate P)ublisher A)ategory
    7- Command line Q)uit
    
    Please type your command:
    .......
    
    '''
    dct = dict()
    filename = 'google_books_dataset.csv'
    file = open(filename)
    data = input('Please type your command(1): ') 
    
    while data.upper() != 'L':
        data = input('File not loaded!\nPlease type your command(2): ')       
    if data.upper() == 'L':
        result1 = book_category_dictionary(filename)
        print(result1) 
        print()
        data = input('Please type your next command(3): ') 
        while data.upper() != 'A':
            data = input('No such command!\nPlease type your command(4): ')  
        if data.upper() == 'A':
            for value in book_category_dictionary(filename).values():
                for i in value:
                    if data in i.get('title'):
                        title = input("Please type title of book: ")
                        author = input("Please type author of book: ")
                        language = input("Please type language of book: ")
                        publisher = input("Please type publisher of book: ")
                        category = input("Please type category of book: ")
                        rating = input("Please type rating of book: ")
                        pages = input("Please type pages of book: ")
                        t = (title,author,language,publisher,category,rating,pages)
                    else:
                        data = input('No such command!\nPlease type your command(4): ')
                result = add_book(dct,t)
                print(result)
                print()
                data = input('Please type your next command(7): ') 
                
                while data.upper() != 'R':
                    data = input('No such command!\nPlease type your command(8): ')  
                if data.upper() == 'R':
                    
                    
                    for value in book_category_dictionary(filename).values():
                        book = value
                        for i in value:
                            if data in i.get('title'):
                                title = input("Please enter book's title that you want to remove: ")
                                result2 = remove_book(book,title,'')
                                print(result2)                    
                                
                                
                                
                            if data in i.get('author'):
                                author = input("Please enter book's author that you want to remove: ")
                                result2 = remove_book(book,'',author)
                                print(result2)                    
                                print()
                                data = input('Shall we continue (Y or N): ')
                                if data.upper() == 'Y':
                                    data = title
                                else:
                                    
                                    print('GoodBye')
                                    file.close()
                                    exit()
                            
                                                                                
                                    
UI_add_remove()
            

# Here is Soliman Elkhouli who is last member of team that dealt with the last case which are Sort books functions. Test functions are not included since they are not asked in the milestone.

def user_interface() -> None:
    """
    User interface that allows user to sort books in terms of different categories such as Title, Author, Category, Rate
    
    >>> Available commands:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
    T)itle R)ate A)uthor P)ublisher C)ategory
    5- GCT) Get all Categories for book Title
    6- S)ort books
    T)itle R)ate P)ublisher A)ategory
    7- Command line Q)uit
    
    Please type your command:
    
    """
    quit = False
    infile = False
    while quit == False:
        commands = ('\nThe available commands are:\n1- L)oad data\n2- A)dd book\n3- R)emove book\n4- G)et books\n  T)itle R)ate A)uthor P)ublisher C)ategory\n5- GCT) Get all Categories for book Title\n6- S)ort books\n   T)itle R)ate P)ublisher C)ategory\n7- Command line Q)uit')
        print(commands)
        
        inp = (input('\nPlease type your command: ')).upper()
        
        if inp == 'L':
            file = input('\nPlease enter the name of the file you want to load: ')
            book = book_category_dictionary(file)
            infile = True
        
        
        
        
        if infile:
            print(commands)
            inp = (input('\nPlease type your command: ')).upper()
            
            if inp == 'N':
                
                if infile:
                    sort_by = (input('How would you like to sort your books?:\nT)itle R)ate P)ublisher A)uthor: ')).upper()
            
                    if sort_by == 'T':
                        print(sort_books_title(book))
                    elif sort_by == 'R':
                        print(sort_books_ascending_rate(book))
                    elif sort_by == 'P':
                        print(sort_books_publisher(book))
                    elif sort_by == 'A':
                        print(sort_books_author(book))
                    else:
                        print('Command does not exist')
                else:
                    print('File not loaded')

        if inp == 'N' and not infile:
            print('File not loaded')
        
        elif inp == 'Q':
            quit = True
        
        else:
            if inp != 'N':
                print('No such command\n')

user_interface()                                  




        
        
    
    
# Fellow teammate Tsu Chen is responsible for the case 2 which contains get_books_by_title, get_books_by_rate, and get_books_by_author. Test functions are not included since they are not asked in the milestone.



def display_commands()->str:
    """
    This function will display the loist of commands avaliable for the user
    Available Commands: 
     1- L)oad data  
     2- G)et books 
      T)itle R)ate A)uthor 
     3- Q)uit
    Please enter a command:
    """    
    print("Available Commands: ")
    print("1- L)oad data" )
    print("2- G)et books")
    print("T)itle R)ate A)uthor")
    print("3- Q)uit")
    
    return input("\nPlease type your command: ")



def get_books():
    """
    
    """
    
    g_book = input("\nPlease enter how to get books: ")
    print('')
    if g_book =="T" or g_book =="t":
        e=input("Please enter the Title of the book: ")
        get_books_by_title(e, load_file)
    elif g_book =="R" or g_book =="r":
        e=input("Please enter the Rating of the book: ")
        get_books_by_rate(load_file, int(e))
    elif g_book =="A" or g_book =="a":
        e=input("Please enter the Author of the book: ")
        get_books_by_author(e, load_file)        
    else:
        print("Command does not exist")
    print("----------------")
    input("\nPress Enter to return to Menu")





i=0
load_file = ''

while i != 'Q' and  i != 'q':
    print('')
    user_input = display_commands()
    if user_input == "Q" or user_input == "q":
        print("End")
        i='q'
    elif user_input == "L" or user_input == "l":
        print("\n---Load File---")
        x = input("\nPlease enter the file name: ")
        load_file = book_category_dictionary(x)
        print("\n---------------------------------")
        print("File has been successfully loaded")
        print("---------------------------------\n")
        input("\nPress Enter to return to Menu")
    elif user_input == "G" or user_input =="g":
        if load_file == '':
            print("**File not loaded**")
            input("\nPress Enter return to Menu")
        else:
            print("\n---Get Books---")
            input("T)itle R)ate A)uthor") 
            get_books()
    else:
        print("\nCommand does not exist")
        input("\nPress Enter to return to Menu")
    
        



