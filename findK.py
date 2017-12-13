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


'''Implements the 'elbow method' to find the optimal number
of clusters to describe the data
https://pythonprogramminglanguage.com/kmeans-elbow-method/
'''

def distanceCalculation(example,cluster):
    oldres = sum([(example[dimension] - cluster.get(dimension,0))**2  for dimension in example.keys()])
    ##print "for examples %s and cluster %s with precomp %f had distance %f" % (example, cluster, precomputation,res)
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
        avg = float(sum(relavant_vals))/len(points)
        if avg > 0: res[dimension] = avg
    return res

examples = []
laterexamples = []
vectorX = []
with open("Period 5 Rand.csv", 'rb') as file_reader:
            reader = csv.reader(file_reader, delimiter = ",")
            counter = 0
            for line in reader:
                if counter == 5000: break #to maintain manageable time
                counter += 1
                vectorX.append(line[1])
                laterObj = (line[0],FeatureExtractor(line[1]).featureVector())
                examples.append(laterObj[1])
                laterexamples.append(laterObj)

extractor = sklearn.feature_extraction.text.CountVectorizer(input = 'content',ngram_range = (2,3),max_df = .7,stop_words = 'english')
X = extractor.fit_transform(vectorX)

distArr = []
inerArr = []
for k in range(1,20):
    clusterer = sklearn.cluster.KMeans(n_clusters = k)
    res = clusterer.fit(X)
    print "Inertia with %d clusters is %d" % (k,clusterer.inertia_)
    inerArr.append(clusterer.inertia_)
    #build the dict-style clusters so I can use my same distortion function consistently across them
    clusters = [0]*k
    for i in range(k):
        total = []
        count = 0
        print "Cluster %d" % i
        for j in range(len(examples)):
            dictOfEx = examples[j]
            if clusterer.labels_[j] == i:
                total.append(dictOfEx)
                count += 1.
        clusters[i] = averageexamples(total)

    distortion = calculateDistortion(examples, clusters, clusterer.labels_)
    print "Distortion"
    print distortion
    distArr.append(distortion)

    
print distArr
plt.figure()
plt.plot(range(1,20),distArr)
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()