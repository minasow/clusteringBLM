import random
import collections
import math
import sys
import csv
import os
from featureExtractor import FeatureExtractor
from spectral import Spectral
from kmeans import Kmeans
import sklearn
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter


def distanceCalculation(example,cluster):
    oldres = (sum([(example[dimension] - cluster.get(dimension,0))**2  for dimension in example.keys()]))
    return oldres

def calculateDistortion(examples,clusters,assignments):
    distortion = 0
    for i in range(len(examples)):
        distortion += distanceCalculation(examples[i], clusters[assignments[i]])
    return distortion

def averageexamples(points):
    res = {}
    keys = list(set([key[0] for point in points for key in point.iteritems()]))
    for dimension in keys:
        relavant_vals = [point[dimension] for point in points]
        avg = float(sum(relavant_vals))/len(relavant_vals)
        if avg > 0: res[dimension] = avg
    return res


examples = []
laterexamples = []
vectorX = []
k = 4

with open("Period 9 Rand.csv", 'rb') as file_reader:
            reader = csv.reader(file_reader, delimiter = ",")
            counter = 0
            for line in reader:
                if counter == 1000: break
                counter += 1
                #raw tweet was line[0]
                #cleaned tweet was line[1]
                vectorX.append(line[1])
                laterObj = (line[0],FeatureExtractor(line[1]).featureVector())
                examples.append(laterObj[1])
                laterexamples.append(laterObj)


#keep the ngrams here in sync with featureExtractor.py, which includes 1-2ngrams
extractor = sklearn.feature_extraction.text.CountVectorizer(input = 'content',ngram_range = (1,3),max_df = 0.95, min_df = .1,stop_words = 'english')
X = extractor.fit_transform(vectorX)

clusterer = sklearn.cluster.SpectralClustering(n_clusters = k)
#clusterer = sklearn.cluster.KMeans(n_clusters = k)
#clusterer = sklearn.cluster.DBSCAN(min_samples = 100)

res = clusterer.fit(X)

#build the dict-style clusters so I can use my same distortion function consistently across them
clusters = [0]*k
counts = Counter(clusterer.labels_)
print(counts)
arr = np.array(clusterer.labels_)
for i in range(k):
    print("Cluster %d" % i)
    indices = np.where(arr == i)[0]
    #exToTake = random.sample(indices,10)
    print("Top ten ngrams:")
    nparr = np.array(examples)
    clusters[i] = averageexamples(nparr[indices])

    #finds the highest weight keywords for each cluster
    d_choices = clusters[i].keys()
    d_probs = clusters[i].values()
    lis = sorted(zip(d_choices,d_probs),key = lambda tup: tup[1])
    one = [x for x in lis if len(x[0]) == 1 and "<hashtag>" not in x[0] and  "<user>" not in x[0] and  "<url>" not in x[0]]
    two = [x for x in lis if len(x[0]) == 2 and "<hashtag>" not in x[0] and  "<user>" not in x[0] and  "<url>" not in x[0]]
    print("one grams")
    print(one[-10:])
    print("bigrams")
    print(two[-10:])
print "Distortion:"
print calculateDistortion(examples, clusters, clusterer.labels_)
