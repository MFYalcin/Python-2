 # Muhammet Furkan Yalcin - 101233944

from T1A1_P3_sorting import sort_books_title
from T1A1_P1_load_data import book_category_dictionary

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
    
   



sort1 = sort_books_title(book_category_dictionary("google_books_dataset.csv"))[0]
sort2 = sort_books_title(book_category_dictionary("google_books_dataset.csv"))[1]
sort3 = sort_books_title(book_category_dictionary("google_books_dataset.csv"))[2]

print('Exercise 1.1: ',sort1)
print('Exercise 1.2: ',sort2)
print('Exercise 1.3: ',sort3)


t1_1 = test_dict('Testing 1.1',{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English\n', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864},{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English\n', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864})
t1_2 = test_dict('Testing 1.2',{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288})
t1_3 = test_dict('Testing 1.3',{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464},{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'language': 'English\n', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464})

print('Testing 1.1: ',t1_1)
print('Testing 1.2: ',t1_2)
print('Testing 1.3: ',t1_3)


