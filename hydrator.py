from twarc import Twarc
from cleanTweets import CleanTweet
import csv
import os

t = Twarc("kW4n41mZ3fi88XihKrOgqWFUL", "cjLInNXO5NK3fXgy7DNYWRyg7E2ZSHpknjye4cDt4As6klvP2U", "3171705764-flvPlj6epMSz4nz5454fONp5nkq4rc3dTqYq9Bs", "vDkMSn9HfPYNcoapZiPcC0ZueN7qDMmn8ZG4xcSqGNPKS")
test_id = ["473172612307509249"]
final_total = 10000 #number of tweets to take from each period
'''Theres a file for every day of the month starting in June 2014,
We want to build a different csv database for each time period (in the project notes),
taking a sample of up to 10,000 tweets from each.'''
def hydrateTweets(period,filename,total,final_total,write_file):
	if total == final_total: return total
	for tweet in t.hydrate(open("bth_ids/Period " + str(period) + "/" + filename)):
		tweet_text = (tweet["full_text"].encode("utf-8"))
		if "RT" not in tweet_text:
			clean_text = CleanTweet(tweet_text).processed()
			#print "Raw text:"
			#print tweet_text
			#print "Clean text:"
			#print clean_text
			write_file.writerow([(tweet_text),(clean_text)])
			total += 1
			if total == final_total: return total
	return total


i = 3
print "on range %d" % i
file_pointer = open("Period " + str(i) + " Rand.csv","wb")
write_file = csv.writer(file_pointer)
files_for_period = os.listdir("bth_ids/Period " + str(i))
total = 0
for j in files_for_period: #go through all files in a period
	print "hydrating file %s" % j
	total = hydrateTweets(i,j,total,final_total,write_file)
		#print "Total is %s" % total
		
'''for tweet in t.hydrate(open('bth_ids/bth_ids_2014-06-01.txt')): #look at tweets from just one of the 365 files
	print "Tweet: "
	print (tweet["full_text"].encode("utf-8"))
	print "Gives a process tweet of: "
	print CleanTweet(tweet["full_text"].encode("utf-8")).processed()
	print "Had %s retweets" % tweet["retweet_count"]'''
