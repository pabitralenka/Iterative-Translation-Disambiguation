__author__ = "Pabitra Lenka"

def conv_bigrams(arg1, arg2):
	unigram, bigram = {}, {}

	with open(arg1) as rf:
		for line in rf:
			line = line.strip()
			line = line.strip("\n")
			line = line.lower()
			text = line.split("\t")
			unigram[text[0]] = int(text[1])

	with open(arg2) as rf:
		for line in rf:
			line = line.strip()
			line = line.strip("\n")
			line = line.lower()
			text = line.split("\t")
			#key = (text[1], text[2])
			text_words = text[0].split()
			key = (text_words[0], text_words[1])
			bigram[key] = int(text[1])

	return unigram, bigram

#Unigram scores from count_1w.txt
#Bigram scores from count_2w.txt
unigram_all, bigram_all = conv_bigrams("count_1w.txt", "count_2w.txt")