import re
def tweet_moodwords(tweet):
	resultdict = {}
	happywords = ['happy','joy','bliss']
	for word in happywords:
		match = re.findall(word, tweet.lower())
		resultdict[word] = len(match)
	return resultdict
