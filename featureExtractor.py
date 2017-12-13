import nltk
import collections
import sys
import re
from nltk import ngrams
#Class that extracts features of a tweet and returns a dictionary
#representing the sparse feature vector.

class FeatureExtractor():
    def __init__(self,raw):
        self.raw = raw

    def featureVector(self):
        return extract(self.raw)


#Takes as input a string (tweet for this project) and returns a dictionary of 
#features
def extract(x):
	d = collections.defaultdict(float)
	tokens = x.split(" ")
	uni_gram = list(collections.Counter(ngrams(tokens,1)))#list(collections.Counter(ngrams(tokens,1))) 
	bi_gram = list(collections.Counter(ngrams(tokens,2))) 
	tri_gram = []#list(collections.Counter(ngrams(tokens,3))) 

	for ngram in uni_gram + bi_gram + tri_gram:
		d[ngram] += 1
	return d