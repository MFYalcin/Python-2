# Muhammet Furkan Yalcin - 101233944

from T1A1_P1_book_category_dictionary import book_category_dictionary
from T1A1_P1_book_category_dictionary import test_dict


filename = 'google_books_dataset.csv'
open(filename)
word_list = book_category_dictionary(filename)
dict1 = word_list['Fiction'][0]
dict2 = word_list['Comics'][0]
dict3 = word_list['Economics'][0]


print('Exercise 1.1: ',dict1)
print('Exercise 1.2: ',dict2)
print('Exercise 1.3: ',dict3)


t1_1 = test_dict('Testing 1.1',{'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating ': 3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288}]}, {'Fiction': [{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating ': 3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288}]})
                  
t1_2 = test_dict('Testing 1.2',{'Comics': [{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96}]},{'Comics': [{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96}]})
t1_3 = test_dict('Testing 1.3',{'Economics': [{'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320}]}, {'Economics': [{'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320}]})

print('Exercise 1.1: ',t1_1)
print('Exercise 1.2: ',t1_2)
print('Exercise 1.3: ',t1_3)

open(filename).close()





