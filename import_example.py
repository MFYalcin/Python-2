import Dictionary_caseStudy_histogram

print("test case")
hist = Dictionary_caseStudy_histogram.build_histogram('whyEnglishIsSoHard.txt')
print(hist)
most_freq_word, frequency = Dictionary_caseStudy_histogram.most_frequent_word(hist)
print("The most frequently occuring word is \"", most_freq_word,
      "\" which occurs", frequency, "times") 