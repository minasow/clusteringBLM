import numpy as np
from scipy import linalg
from sklearn.cluster import KMeans
import math

class Spectral():
    def __init__(self,x):
        self.x = x #the list of Xi's

    def clustering(self):
        return cluster(self.x)


def cluster(X):
	stdev = 1
	k = 4

	def buildAffinity(i,j):
		if(i==j):
			return 0.
		else:
			norm = sum([(X[i][dimension] - X[j][dimension])**2  for dimension in X[i].keys()])
			return np.exp((-1*norm)/(2*stdev))
	def distanceCalculation(example,cluster):
		oldres = math.sqrt(sum([(example[dimension] - cluster[dimension])**2  for dimension in example.keys()]))
		return oldres
	def calculateDistortion(examples,clusters,assignments):
		distortion = 0
		for i in range(len(examples)):
			distortion += distanceCalculation(examples[i], clusters[assignments[i]])
		return distortion

	lossArr = []
	loss = 0 #calcdistortion
	clusters = []
	assignments = [0]*len(X)

	f = np.vectorize(buildAffinity)
	affMatrix = np.fromfunction(lambda i,j: f(i,j),(len(X),len(X)),dtype = int)

	def buildD(i,j):
		if(i == j):
			return sum(affMatrix[i])
		else:
			return 0.

	g = np.vectorize(buildD)
	dMatrix = np.fromfunction(lambda i,j: g(i,j),(len(X),len(X)),dtype = int)
	dPowered = linalg.fractional_matrix_power(dMatrix,(-.5))
	lMatrix = np.matmul(dPowered,np.matmul(affMatrix,dPowered))
	eigenvals, Xarr = linalg.eigh(lMatrix,eigvals = (0,k-1))
	norms = np.linalg.norm(Xarr, axis = 1, keepdims = True)
	Y = Xarr / norms
	print Y.shape
	kmeans = KMeans(n_clusters = k).fit(Y)

	for i in range(len(X)):
		assignments[i] = kmeans.labels_.tolist()[i]
	print "Distortion is"
	print calculateDistortion(X,kmeans.cluster_centers_.tolist(),assignments)
	return kmeans.cluster_centers_.tolist(),assignments,kmeans.inertia_, lossArr