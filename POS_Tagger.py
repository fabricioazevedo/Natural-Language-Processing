import nltk

#This 

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''
		
	
def learnDefaultTagger(simpleSentence):
	wordsInSentence = nltk.word_tokenize(simpleSentence)
	tagger = nltk.DefaultTagger("NN")
	posEnabledTags = tagger.tag(wordsInSentence)
	print(posEnabledTags)

def learnRETagger(simpleSentence):
	customPatterns = [       #a variable called customPatterns
	(r'.*ing$', 'ADJECTIVE'),  # a new Python list datatype
	(r'.*ly$', 'ADVERB'),
	(r'.*ion$', 'NOUN'),  # Each element in this list is a tuple that has two items in it
	(r'(.*ate|.*en|is)$', 'VERB'), # The first item in the tuple is a regular expression
	(r'^an$', 'INDEFINITE-ARTICLE'), #The second item in the tuple is a string
	(r'^(with|on|at)$', 'PREPOSITION'),
	(r'^\-?[0-9]+(\.[0-9]+)$', 'NUMBER'),
	(r'.*$', None),
	]
	tagger = nltk.RegexpTagger(customPatterns)
	wordsInSentence = nltk.word_tokenize(simpleSentence)
	posEnabledTags = tagger.tag(wordsInSentence)
	print(posEnabledTags)
	
def learnLookupTagger(simpleSentence):
	mapping = {
		'.': '.', 'place': 'NN', 'on': 'IN',
		'earth': 'NN', 'Mysore' : 'NNP', 'is': 'VBZ',
		'an': 'DT', 'amazing': 'JJ'
	}
	tagger = nltk.UnigramTagger(model=mapping)
	wordsInSentence = nltk.word_tokenize(simpleSentence)
	posEnabledTags = tagger.tag(wordsInSentence)
	print(posEnabledTags)
	
if __name__ == '__main__':
	
	testSentence = "Mysore is an amazing place on earth. I have visited Mysore 10 times."

	learnDefaultTagger(testSentence)
	learnRETagger(testSentence)
	learnLookupTagger(testSentence)
