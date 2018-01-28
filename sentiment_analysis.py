from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import matplotlib.pyplot as plt

sid = SentimentIntensityAnalyzer()

def main():
	#open the data text file
	f = open("data.txt", "r")
	data = f.read()

	#load the data as dictionary
	dataDict = json.loads(data)

	#get polarity scores of all data
	scores = analyze_submissions(dataDict)

	#count the number of submissions gathered
	count = 0

	scores_list = []

	for score in scores:
		scores_list.append(score['compound'])
		count += 1

	#plot the scores
	plt.plot(scores_list, [0] * count, 'ro')
	plt.axis([-1, 1, 0, 0])
	plt.show()

def analyze_submissions(data):
	for key, value in data.items():
		yield sid.polarity_scores(key)

if __name__ == "__main__":
	main()