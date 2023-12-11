import nltk

nltk.download("wordnet")

from nltk.corpus import wordnet

# Get synsets (sets of synonyms) for a word
synsets = wordnet.synsets("mgcv")

# Print information about each synset
for synset in synsets:
    print("Synset:", synset.name())
    print("Definition:", synset.definition())
    print("Examples:", synset.examples())
    print()
