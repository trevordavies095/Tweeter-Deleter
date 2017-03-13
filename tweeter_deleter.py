"""
Name       : Loren Davies
Program    : Tweeter Deleter
Description: Deletes tweets based on specified keywords.
Date       : March 12th, 2017
"""

from twython import Twython
from twython import TwythonError
import argparse
import time
import os

def term_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("twitter_handle", type=str, help="twitter handle")
	parser.add_argument("keyword_file", type=str, help="text file containing keywords")
	return parser.parse_args()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def keyword_remover(twitter, username, file):
	f = open(file, "r")
	words = []
	ids = []
	count = 0
	deleted = 0

	for line in f:
		line = line.strip()
		words.append(line)
	f.close()

	user_timeline = twitter.get_user_timeline(screen_name=username, count=1, include_retweets=False)

	for tweet in user_timeline:
		if count == 0:
			ids.append(tweet['id'])

	clear()
	print("Deleting tweets...")

	for i in range(0, 16):
		user_timeline = twitter.get_user_timeline(screen_name=username, count=200, include_retweets=False, max_id=ids[-1])
		for tweet in user_timeline:
			for i in range(0, len(words)):
				if words[i] in tweet['text'].lower():
					try:
						twitter.destroy_status(id=tweet['id'])
						deleted += 1
						continue
					except TwythonError:
						print("Tweet already deleted...")
				else:
					ids.append(tweet['id'])
			count += 1
		clear()
		print("Deleting tweets...")
		print("Tweets deleted: " + str(deleted))
		print("Tweets checked: " + str(count))
		time.sleep(300)

	print("Tweets deleted!")


def main():
	consumer_key        = ""	# Twitter app credentials
	consumer_key_secret = ""
	access_token        = ""
	access_token_secret = ""
	args = term_args()

	twitter = Twython(consumer_key, consumer_key_secret, access_token, access_token_secret)
	keyword_remover(twitter, args.twitter_handle, args.keyword_file)


if __name__ == "__main__":
    main()
