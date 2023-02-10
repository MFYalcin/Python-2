
import string

def book_authors_dictionary(filename: str) ->dict:

    """
     precondition: file must be .csv or .txt and contain information in the same layout as the file in example

     Returns the different types of books and the information about them based on the author
    """
    infile = open(filename)
    book_dictionary=dict()
    authors = set()
    lst = []
    for line in infile:
        word_list = line.strip(string.punctuation).split(",")
        authors.add(word_list[1])

        rating = word_list[2]
        if rating != "N/A" and rating!="rating":
            rating = float(rating)
        else:
            rating = ""

        pages = word_list[4]
        if pages != "pages":
            pages = int(pages)
        else:
            pages = ""
        lst.append({"title ": word_list[0],"language ":word_list[6],
        "rating ": rating, "publisher ": word_list[3],"category ": 
        word_list[5],"pages ":pages})

        for book in line:
            if word_list[1] not in book_dictionary:
                author = word_list[1]
                book_dictionary[author] = lst
        lst=[]

    book_dictionary.pop(author)
    return book_dictionary


filename = 'google_books_dataset.csv'
word_list = book_authors_dictionary(filename)
print('File', filename, 'contains', len(word_list), 'distinct words')
print('The book categories in this file is:', word_list)