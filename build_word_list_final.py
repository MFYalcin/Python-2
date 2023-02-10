"""
ECOR 1042
Case study: iterative, incremental development of a function that uses
Python's str, list, and set types.
"""
import string
from typing import List

# For information about the string module
# - type help(string) at the shell prompt, or 
# - read 'Practical Programming', Chapter 7, 'Using Methods'

def build_word_list(filename: str) -> List[str]:
    """Return a list of all the distinct words in the specified file,
    sorted in ascending order.
    
    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    >>> len(word_list)  # How many different words are in the file?
    """
    # The final iteration demonstrates that we can read a line from a text file
    # and split the line into a list of words. For each word in the list,
    # we remove any punctuation marks before or after the word, convert 
    # the word to lower case, then put the word in a set. (This is a simple
    # way to discard duplicate words).
    # This is repeated until every line has been read and processed, after
    # which a new list is created, using the words from the set.
    # The list is then sorted and returned. We're done!
    
    infile = open(filename, "r")
    word_set = set()

    for line in infile:

        # Split each line into a list of words.
        # By default, the split method removes all whitespace; e.g.,
        # '  Hello,    world!   '.split() returns this list:
        #
        #    ['Hello,', 'world!']
        #
        # and not:
        #
        #    ['  Hello,', '    world!   ']
        #
        # Notice that the punctuation marks have not been removed.
        
        word_list = line.split()

        # For each word, first remove any leading or trailing punctuation,
        # then convert the the word to lower case.
        #
        # Examples: 
        #  'Hello,'.strip(string.punctuation) returns 'Hello'.
        #  'Hello'.lower() returns 'hello'.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            # This statement is equivalent to: 
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Don't save any empty strings that were created when the 
            # punctuation marks were removed.
            # For example, if word is bound to a hyphen, '-',
            # word.strip(string.punctuation) yields the empty string, ''.
            
            if word != '':
                # Storing the words in a set discards any duplicates.
                word_set.add(word)

    infile.close()
    
    # Now build the list of distinct words.  
    word_list = list(word_set)
    
    # or,
    # word_list = []
    # for word in word_set:
    #    word_list.append(word)

    # Sort the list into ascending order.
    word_list.sort()
    
    return word_list

filename = 'whyEnglishIsSoHard.txt'
word_list = build_word_list(filename)
print('File', filename, 'contains', len(word_list), 'distinct words')
print('The words are:', word_list)

filename2 = 'sons_of_martha.txt'
word_list2 = build_word_list(filename2)
print('File', filename2, 'contains', len(word_list2), 'distinct words')
print('The words are:', word_list2)
