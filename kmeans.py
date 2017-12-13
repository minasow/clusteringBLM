import random
import collections
import math
import sys
import csv
import os

#Kmeans clustering from CS221

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
            ##print dimension
            relavant_vals = [point[dimension] for point in points]
            #print relavant_vals
            ##print relavant_vals
            avg = float(sum(relavant_vals))/len(points)
            if avg > 0: res[dimension] = avg
            #print res[dimension]
        ##print "res is %s" % res
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

'''def kmeans(examples, K, maxIters):
    
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    
    # BEGIN_YOUR_CODE (our solution is 32 lines of code, but don't worry if you deviate from this)
    def precompute(clusters):
    	res = [0]*len(clusters)
    	for i in range(len(clusters)):
    		cluster = clusters[i]
    		squared_sum = 0
    		for dimension in cluster.keys():
    			squared_sum += (cluster[dimension]**2)
    		res[i] = squared_sum
    	return res

    def calculateLoss(examples,clusters,assignments,precomputations):
    	res = 0
    	for i in range(len(examples)):
    		res += distanceCalculation(examples[i], clusters[assignments[i]], precomputations[assignments[i]])
    	return res

    def distanceCalculation(example, cluster, precomputation):
    	#oldres = math.sqrt(sum([(example[dimension] - cluster.get(dimension,0))**2  for dimension in example.keys()]))
    	phi_squared = sum([example[i]**2 for i in example.keys()])
    	res = math.sqrt(phi_squared + precomputation - 2*dotProduct(example,cluster))
    	##print "for examples %s and cluster %s with precomp %f had distance %f" % (example, cluster, precomputation,res)
    	return res

    def averagingCluster(points): #LOOK HERE MAYBE
    	res = {}
        keys = [key[0] for point in points for key in point.iteritems()]
    	for dimension in keys:
            ##print dimension
            relavant_vals = [point[dimension] for point in points]
            #print relavant_vals
    		##print relavant_vals
            res[dimension] = float(sum(relavant_vals))/len(points)
            #print res[dimension]
        ##print "res is %s" % res
        return res


    clusters = (random.sample(list(examples), K))
    assignments = [0] * len(examples)
    precomputations = precompute(clusters)
    loss = calculateLoss(examples, clusters, assignments, precomputations)
    ##print "for examples %s clusters %s had loss %f" % (examples,clusters,loss)

    for m in range(maxIters):
    	pastLoss = loss
    	for i in range(len(examples)):
            distances = [distanceCalculation(examples[i], cluster, precomputations[clusters.index(cluster)]) for cluster in clusters]
            assignments[i] = distances.index(min(distances))
        #print assignments
    	for j in range(len(clusters)):
            assigned_points = [examples[k] for k in range(len(examples)) if assignments[k] == j]
            old = clusters[j]
            if(len(assigned_points) > 0):
                clusters[j] = averagingCluster(assigned_points)
                if clusters[j] == old: #print "DOES NOT CHANGE"
    	precomputations = precompute(clusters)
    	loss = calculateLoss(examples, clusters, assignments, precomputations)
        #print "Loss after %d iterations: %d" % (m,loss)
    	#if loss == pastLoss: break
    return (clusters,assignments, loss)
    # END_YOUR_CODE


def dotProduct(d1, d2):
    if len(d1) < len(d2):
        return dotProduct(d2, d1)
    else:
        return sum(d1.get(f, 0) * v for f, v in d2.items())'''


