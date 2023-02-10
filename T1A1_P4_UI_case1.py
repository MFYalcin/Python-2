# Muhammet Furkan Yalcin - 101233944
from T1A1_P1_load_data import book_category_dictionary
from T1A1_P2_fun import add_book
from T1A1_P2_fun import remove_book

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
                            
                                                                                
                                    

            

                                    
                
                        
            
       
        
        
    
    



