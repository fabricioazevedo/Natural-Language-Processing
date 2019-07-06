from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tokenize import  sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import time
import pandas as pd
from collections import defaultdict
#-----------------------------------------------/// ---------------------------------------------------------------#
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
		
# lemmatizer = WordNetLemmatizer()
# lemmatizer.lemmatize('going', wordnet.VERB)
#------------------------------------------------- //// -----------------------------------------------------------#
# tag_map = defaultdict(lambda : wn.NOUN)
# tag_map['J'] = wn.ADJ
# tag_map['V'] = wn.VERB
# tag_map['R'] = wn.ADV

lemmatizer = WordNetLemmatizer()

with open('20words.txt') as f:
    file_token = f.read()

text1 = "guru99 is a totally new kind of learning experience."
text2 = "studies studying cries cry"

wordLemmas = pos_tag(word_tokenize(file_token))
print(wordLemmas)

lemmas = open('words.txt','w')

for w,tag in wordLemmas:
	if w:
		wntag = tag[0].lower()
		wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
		if not wntag:
			lemma = w
		else:
			lemma = lemmatizer.lemmatize(w, wntag)		
			lemma = lemmatizer.lemmatize(w,tag_map[tag[0]]) #Enter tags in wordnet format
			print("Lemma for {} is {}".format(w, lemma))
			lemmas.write(lemma)
			lemmas.write("\n")
		
list_w = [] # words
list_d = [] # sentences
list_syn = [] # synonymous
list_ex = [] #example

with open('words.txt') as f:
    list_words = f.read().split()
	
# Real Time example showing use of Wordnet Lemmatization and POS Tagging in Python

# from nltk.corpus import wordnet as wn
	# from nltk.stem.wordnet import WordNetLemmatizer
	# from nltk import word_tokenize, pos_tag
	# from collections import defaultdict
	# tag_map = defaultdict(lambda : wn.NOUN)
	# tag_map['J'] = wn.ADJ
	# tag_map['V'] = wn.VERB
	# tag_map['R'] = wn.ADV

	# text = "guru99 is a totally new kind of learning experience."
	# tokens = word_tokenize(text)
	# lemma_function = WordNetLemmatizer()
	# for token, tag in pos_tag(tokens):
		# lemma = lemma_function.lemmatize(token, tag_map[tag[0]])
		# print(token, "=>", lemma)
	

# To resolve the problem, always POS-tag your data before lemmatizing, e.g.

 # from nltk.stem import WordNetLemmatizer 
 # from nltk import pos_tag, word_tokenize
 # wnl = WordNetLemmatizer()
 # sent = 'This is a foo bar sentence'
 # pos_tag(word_tokenize(sent))
# [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('foo', 'NN'), ('bar', 'NN'), ('sentence', 'NN')]
 # for word, tag in pos_tag(word_tokenize(sent)):
     # wntag = tag[0].lower()
     # wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
     # if not wntag:
             # lemma = word
     # else:
             # lemma = wnl.lemmatize(word, wntag)
     # print lemma

