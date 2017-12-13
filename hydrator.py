from twarc import Twarc
from cleanTweets import CleanTweet
import csv
import os

t = Twarc("<SENSITIVE TWITTER KEY INFORMATION>")
test_id = ["<SENSITIVE TWITTER KEY INFORMATON>"]
final_total = 10000 #number of tweets to take from each period

'''Theres a file for every day of the month starting in June 2014,
We want to build a different csv database for each time period (in the project notes),
taking a sample of up to 10,000 tweets from each.'''

def hydrateTweets(period,filename,total,final_total,write_file):
	if total == final_total: return total
	for tweet in t.hydrate(open("bth_ids/Period " + str(period) + "/" + filename)):
		tweet_text = (tweet["full_text"].encode("utf-8"))
		if "RT" not in tweet_text: #exclude retweets
			clean_text = CleanTweet(tweet_text).processed()
			write_file.writerow([(tweet_text),(clean_text)])
			total += 1
			if total == final_total: return total
	return total


for i in range(1,10):
	print "On time period: %d" % i
	file_pointer = open("Period " + str(i) + ".csv","wb")
	write_file = csv.writer(file_pointer)
	files_for_period = os.listdir("bth_ids/Period " + str(i))
	total = 0
	for j in files_for_period: #go through all files in a period
		print "Hydrating file %s" % j
		total = hydrateTweets(i,j,total,final_total,write_file)