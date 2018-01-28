import praw, json

#script for writing the first 25 posts on /r/suicidewatch
#and /r/happy to a text file

def main():
	r = praw.Reddit('bot1')
	print("Configured Reddit bot.")

	f = open('data.txt', 'w');

	suicide_watch = r.subreddit('suicidewatch')
	suicide_watch_subs = suicide_watch.hot(limit=25)
	#suicide_watch_subs = suicide_watch.submissions(1509723947, 1509810347)

	data_dictionary = {}

	print("/r/suicidewatch")

	for submissions in suicide_watch_subs:
		data_dictionary[submissions.selftext] = "depressed";
		#f.write(submissions.selftext)
		print(submissions.selftext)

	print("\n\n")

	print("/r/happy")

	happy = r.subreddit('happy')
	happy_subs = happy.hot(limit=25)

	for submissions in happy_subs:
		data_dictionary[submissions.title] = "not depressed";
		print(submissions.selftext)

	print("\n\n")

	jsonData = json.dumps(data_dictionary)
	f.write(jsonData)

	f.close()

if __name__ ==  "__main__":
	main()