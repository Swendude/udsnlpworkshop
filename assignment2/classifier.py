import nltk, csv, random

# We are going to use this list to open the datafile
dataset = []
# Open the file and prepare the data
with open('Sentiment Analysis Dataset.csv','rb') as datasetfile:
	datareader = csv.reader(datasetfile, delimiter=",", quotechar='"')
	for row in datareader:
		if row[1] == "1":
			dataset.append((row[3], "positive"))
		else:
			dataset.append((row[3], "negative"))

# Feature functions go here:

def tweet_feature(tweet):
	return {"last":tweet[-1]}

# Feature functions end here
# Let's create a featurelist
featureset = ([(tweet_feature(tweet.strip()), label) for (tweet, label) in dataset])
print 

# Let's create a trainset and a testset
random.shuffle(featureset)
train_set, test_set = featureset[:-100], featureset[-100:]

# Let's train and test accuracy! Also print some information about wich features help the most!
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)