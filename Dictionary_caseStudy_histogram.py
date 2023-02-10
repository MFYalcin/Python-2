"""
ECOR 1042 - Using a Dictionary to Implement a Histogram
"""
import string
from typing import Dict, Tuple

def build_histogram(filename: str) -> Dict[str, int]:
    """Return a histogram of the words in the specified file.
    (A histogram is a set of counters. In this example, each counter
    keeps track of the number of occurrences of one word.)
     
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    """

    infile = open(filename, "r")
    hist = {}

    for line in infile:

        # Split each line into a list of words.
        # The split method removes the whitespace from around each word.
        
        word_list = line.split()

        # For each word, remove any punctuation marks immediately
        # before and after the word, then convert it to lower case.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            # or, 
            # word = word.strip(string.punctuation)
            # word = word.lower()
           
            if word != '':
                count = hist.get(word, 0)  # get returns the current count of
                                           # the number of occurrences of word, 
                                           # or if word is not yet in the 
                                           # dictionary set count to 0
                hist[word] = count + 1

            # or simply,
            # hist[word] = hist.get(word, 0) + 1

    return hist


def most_frequent_word(hist: Dict[str, int]) -> Tuple[str, int]:
    """Return a tuple containing the most frequently occurring word in the 
    specified histogram (a dictionary of word/frequency pairs), along with its 
    frequency.
    
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> word, count = most_frequent_word(hist)  # Which word occurs most often?    
    """
    max_frequency = -1
    for word in hist:
        if hist[word] > max_frequency:
            max_frequency = hist[word]
            most_frequent = word
    
    return (most_frequent, max_frequency)

if __name__ == '__main__':
    hist = build_histogram('sons_of_martha.txt')
    print(hist)
    most_freq_word, frequency = most_frequent_word(hist)
    print("The most frequently occuring word is \"", most_freq_word,
          "\" which occurs", frequency, "times") 
