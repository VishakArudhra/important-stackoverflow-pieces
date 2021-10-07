
#code for making bigrams

###first 

text = ["this is a sentence", "so is this one"]
bigrams = [b for l in text for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
print(bigrams)
# [('this', 'is'), ('is', 'a'), ('a', 'sentence'), ('so', 'is'), ('is', 'this'), ('this',     
'one')]

###using nltk

from nltk import word_tokenize 
from nltk.util import ngrams


text = ['cant railway station', 'citadel hotel', 'police stn']
for line in text:
    token = nltk.word_tokenize(line)
    bigram = list(ngrams(token, 2)) 

    # the '2' represents bigram...you can change it to get ngrams with different size
