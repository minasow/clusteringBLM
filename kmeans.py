import random
import collections
import math
import sys
import csv
import os

#Kmeans clustering implementation

class Kmeans():
    def __init__(self,x,k,iters):
        self.x = x #the list of Xi's
        self.k = k
        self.iters = iters

    def clustering(self):
        return kmeans(self.x,self.k,self.iters)


def kmeans(examples,K,maxIters):

    def distanceCalculation(example,cluster):
        oldres = math.sqrt(sum([(example[dimension] - cluster.get(dimension,0))**2  for dimension in example.keys()]))
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

    lossArr = []
    mu = random.sample(examples,K) #pick k random examples, and 
    c = [0]*len(examples) #c[i] = j where mu[j] is the cluster nearest example[i]
    distortion = calculateDistortion(examples,mu,c)
    print "Distortion of %f" % distortion
    lossArr.append(distortion)
    for each_iter in range(maxIters):
        print "iter"
        for i in range(len(c)):
            distance = [distanceCalculation(examples[i], cluster) for cluster in mu]
            c[i] = distance.index(min(distance))
            #assign c[i] to the nearest cluster
        for j in range(len(mu)):
            examples_assigned = [examples[i] for i in range(len(examples)) if c[i] == j]
            if(len(examples_assigned) > 0): mu[j] = averageexamples(examples_assigned) 

        #redefine mu[j] to the average of its assigned points 
        new_distortion = calculateDistortion(examples,mu,c)
        if new_distortion == distortion : break
        distortion = new_distortion
        print "Distortion of %f" % distortion
        lossArr.append(distortion)



    return mu, c, distortion, lossArr
