filename = 'practice.txt'
import string


def histogram_txt(filename:str) -> dict:
    infile = open(filename)
    hist = {}
    
    for line in infile:
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            if word != '':
                count = hist.get(word,0)
                hist[word] = count + 1
    return hist
        


def freq_word(hist: dict)->tuple:
    max_freq = -1
    for word in hist:
        if hist[word] > max_freq:
            max_freq = hist[word]
            most_freq = word
    return (most_freq,max_freq)


if __name__=='__main__':
    hist = histogram_txt(filename)
    print(hist)
    most_freq,freq = freq_word(hist)
    print("The most frequently occuring word is\"", most_freq,
  "\" which occurs", freq, "times")

