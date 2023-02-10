# Muhammet Furkan Yalcin - 101233944

from T1A1_P2_fun import test_dict
from T1A1_P2_fun import test_str
from T1A1_P2_fun import add_book
from T1A1_P2_fun import remove_book
from T1A1_P2_fun import get_books_by_category



add1 = add_book({'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},('title','author','rating','publisher','pages','category','language'))
add2 = add_book({'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},('title','author','rating','publisher','pages','category','language'))
add3 = add_book({'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},('title','author','rating','publisher','pages','category','language'))

print('Exercise 1.1: ',add1)
print('Exercise 1.2: ',add2)
print('Exercise 1.3: ',add3)


t1_1 = test_dict('Testing 1.1',{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},{'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288})
                  
t1_2 = test_dict('Testing 1.2',{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},{'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96})
t1_3 = test_dict('Testing 1.3',{'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},{'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320})

print('Exercise 1.1: ',t1_1)
print('Exercise 1.2: ',t1_2)
print('Exercise 1.3: ',t1_3)


rmv1 = remove_book({'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},'title','author')
rmv2 = remove_book({'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},'title','author')
rmv3 = remove_book({'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},'title','author')

print('Exercise 2.1: ',rmv1)
print('Exercise 2.2: ',rmv2)
print('Exercise 2.3: ',rmv3)

t2_1 = test_dict('Testing 2.1',{'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},{'author': 'Barbara Allan', 'language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288})
                  
t2_2 = test_dict('Testing 2.2',{'author': 'Cullen Bunn', 'language': 'English', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},{'author': 'Cullen Bunn', 'language': 'English', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96})
t2_3 = test_dict('Testing 2.3',{'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},{'author': 'Dale Carnegie', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320})

print('Exercise 2.1: ',t2_1)
print('Exercise 2.2: ',t2_2)
print('Exercise 2.3: ',t2_3)

ctg1 = get_books_by_category({'title ': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan','category':'Fiction','language': 'English\n', 'rating ': 3.3, 'publisher ': 'Kensington Publishing Corp.', 'pages ': 288},'category')
ctg2 = get_books_by_category({'title ': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn','category':'Fiction', 'language': 'English\n', 'rating ': 4.2, 'publisher ': 'Marvel Entertainment', 'pages ': 96},'category')
ctg3 = get_books_by_category({'title ': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie','category':'Fiction', 'language': 'English\n', 'rating ': 4.3, 'publisher ': 'Simon and Schuster', 'pages ': 320},'category')

print('Exercise 3.1: ',ctg1)
print('Exercise 3.2: ',ctg2)
print('Exercise 3.3: ',ctg3)

t3_1 = test_str('Testing 3.1',"Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan","Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan")
t3_2 = test_str('Testing 3.2',"Book 2: The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett","Book 2: The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett")
t3_3 = test_str('Testing 3.3',"Book 3: Edgedancer: From the Stormlight Archive by Brandon Sanderson","Book 3: Edgedancer: From the Stormlight Archive by Brandon Sanderson")

print('Exercise 3.1: ',t3_1)
print('Exercise 3.2: ',t3_2)
print('Exercise 3.3: ',t3_3)
