# python module to analyze a given text file containing a book for its vocabulary frequency and display the most
# frequent words to the user

import string

dic_of_words = {}

with open('pg6422.txt', 'r') as file:
    lines = file.read().lower()

translator = str.maketrans('', '', string.punctuation)
string_without_punct = lines.translate(translator)
# print(string_without_punct)
words = string_without_punct.count(" ")
for w in string_without_punct:
    count = 1
    if w in dic_of_words:
        dic_of_words.update({w: count})
        count += 1
    else:
        dic_of_words[w] = 1


# dic_of_words[i]
print(dic_of_words)
print(words)
