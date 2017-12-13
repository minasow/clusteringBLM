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

examples = []
laterexamples = []
vectorX = []
with open("Period 4 Rand.csv", 'rb') as file_reader:
            reader = csv.reader(file_reader, delimiter = ",")
            counter = 0
            for line in reader:
            	#if counter == 1000: break
            	counter += 1
            	#print line
                #examples.append(extractWordFeatures(line[0]))
                #print "raw tweet was"
                #print line[0]
                #print "cleaned tweet was "
                #print line[1]
                vectorX.append(line[1])
                laterObj = (line[0],FeatureExtractor(line[1]).featureVector())
                #print "featurevector was"
                #print str(obj)
                examples.append(laterObj[1])
                laterexamples.append(laterObj)

vectorX = list(set(vectorX))
extractor = sklearn.feature_extraction.text.CountVectorizer(input = 'content',ngram_range = (2,3),max_df = .7,stop_words = 'english')
X = extractor.fit_transform(vectorX)

print extractor.stop_words
print X.shape
svd = sklearn.decomposition.TruncatedSVD(n_components = 50) #in place of PCA, another dimensionality reduction program, since it's a sparse matrix
svd.fit(X)
tsne = sklearn.manifold.TSNE(n_components = 3).fit_transform(svd.components_)
print tsne.shape
figure = plt.figure()
ax = figure.add_subplot(111,projection = '3d')
ax.scatter(tsne[:, 0], tsne[:, 1], tsne[:,2])
plt.show()