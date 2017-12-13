# clusteringBLM

Using clustering analysis to further explore online discussions of race. Final project for CS 229: Machine Learning Fall 2017

Files:



Analysis:


runClustering.py: Overarching program that runs clustering on all time periods and reports results of cluster features.

visualizeData.py: Using Principal Component Analysis and TSNE to display the data's principal components, and get a sense for the spacing. 

findK.py: Runs multiple iteration of whichever clustering algorithm is being run, reporting on results in graph so we can apply the 'elbow method' and decide on number of clusters k systematically.




Data Collection, Formatting and Prepping


hydrator.py: Using Tweet ids from "Beyond The Hashtag" and the Twitter API, "rehydrates" to get full tweet objects and save them as csv in working directoy for use in analyses.

cleanTweets.py: In charge of preprocessing for tweets. An extension of Stanford Preprocessing Script, to include stopwords from stopWords.txt and Porter stemming to clean up data. 

featureExtractor.py: Takes a string Tweet and returns a dictionary representation of all unigrams and bigrams (includes commented out ability to include trigrams)

port.py: An implementation of the Porter stemming algorithm. See details at http://www.tartarus.org/~martin/PorterStemmer




Personal Implementations:


spectral.py: Spectral clustering implementation using the sklearn.KMeans implementation.

kmeans.py: From-scratch implementation of KMeans.



