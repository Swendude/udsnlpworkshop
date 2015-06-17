my_file = open('obama.txt','rb')

styledict = {}

textstring = my_file.read().replace("\n", " ")
splittext = textstring.split()

for (i, word) in enumerate(splittext):
	

# for line in my_file:
# 	wordlist = line.split()
# 	for word in enumerate(wordlist):
# 		print word
# 		# if word in styledict.keys():




# # KEY - VALUES
# # 'MY' - ['Fellow','wife']
# # 'fellow' - ['Citizens:']

# # We start with the first word: "My"
# # do this 200 times:
# # Pick a random word from the value list
# # select the last word added as currentword