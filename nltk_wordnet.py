from nltk.corpus import wordnet as wn


chair = 'chair'

chair_synsets = wn.synsets(chair)
print('Synsets/Senses of Chair :', chair_synsets, '\n\n')

for synset in chair_synsets[:2]:
	print(synset, ': ')
	print('Definition: ', synset.definition())
	print('Lemmas/Synonymous words: ', synset.lemma_names())
	print('Example: ', synset.examples(), '\n')