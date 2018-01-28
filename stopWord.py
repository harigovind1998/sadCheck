import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
file = open("data.txt")
line = file.read()# Use this to read file content as a stream:
words = line.split()
for s in words:
    if not (s in stop_words):
        appendFile = open('filteredtext.txt', 'a')
        appendFile.write(s + " ")
        appendFile.close()