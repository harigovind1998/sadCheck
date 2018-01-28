import praw, json

#script for writing the first 25 posts on /r/suicidewatch to a text file

def main():
	r = praw.Reddit('bot1')
	print("Configured Reddit bot.")

	f = open('data.txt', 'w');

	suicide_watch = r.subreddit('suicidewatch')
	suicide_watch_subs = suicide_watch.hot(limit=25)
	#suicide_watch_subs = suicide_watch.submissions(1509723947, 1509810347)

	data_dictionary = {}

	count = 0;

	for submissions in suicide_watch_subs:
		data_dictionary[count] = submissions.selftext
		count += 1
		#f.write(submissions.selftext)
		print(submissions.selftext)

	jsonData = json.dumps(data_dictionary)
	f.write(jsonData)

	f.close()

if __name__ ==  "__main__":
	main()