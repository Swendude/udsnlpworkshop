import random

# A dictionary
# Keys: Individual words
# Values: List of words that may follow on the key
styledict = {}

# This is how you open a file in Python. It will return a iterable of lines in the file.
textfile = open("willem-alexander.txt",'rb')

# This code will put the whole text into a string
textstring = textfile.read().replace("\n", " ")
words = textstring.split()	
# What we need to do now is add every word to the dictionary as a key, then add the next word to the values
# The enumerate function takes a list and adds the indexes to the words. That way we can keep track of our position in the list
for i, word in enumerate(words):
	currentindex = i
	currentword = word
	# We need to check if the line has ended
	if i+1 < len(words):
		# We need to check if we already added the word to our styledict as a key. 
		if word in styledict.keys():
			# if the word is already in the dict we add the next word to the list
			styledict[word].append(words[i+1])
		else:
			# else we add it to the dict and make a list with the next word in it.
			styledict[word] = [words[i+1]]
# So now we have a styledict!
# for key, value in styledict.items():
# 	print key, value

# We are now going to generate a new text! We need a starting point. The empty string: ""
# We need to add a possible follow word aswell.

styledict[""] = [words[0]]
currentword = ""
resultstring = ""
# Let's make it 200 words long.
for i in range(200):
	currentword = random.choice(styledict[currentword])
	resultstring = resultstring + " " + currentword
	# Just something to make it look nice, nothing special!
	if currentword[-1] == "." or currentword[-1] == ",":
		resultstring = resultstring + "\n"

print resultstring



