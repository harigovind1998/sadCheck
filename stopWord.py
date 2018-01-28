import io
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def main():
	stop_words = set(stopwords.words('english'))
	file = open('data.txt')
	line = file.read()
	words = line.split()
	for s in words:
		if not s in stop_words:
			appendFile=open('filteredtext.txt','a')
			appendFile.write(s + " ")
			appendFile.close()
	file.close()
	file2=open('filteredtext.txt','r').read()
	jsonObj = json.loads(file2)
	print(jsonObj)

if __name__ ==  "__main__":
	main()
