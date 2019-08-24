"""Collects tweets"""
import tweepy as tp
import mykeys as mk
import re
import pickle
import random
import numpy as np
import csv
import time
import unicodedata
auth = tp.AppAuthHandler(mk.CONSUMER_KEY,mk.CONSUMER_SECRET)
api = tp.API(auth,wait_on_rate_limit=True)
sentence_list = []
def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tp.RateLimitError:
            print("hit limit, waiting 15 min...")
            time.sleep(15*60)
# Get tweets and split them with #entrepreneurlife
for tweet in tp.Cursor(api.search,q='#entrepreneurship',lang="en",result_type="mixed",tweet_mode="extended").items(50000):
    text = ""
    if hasattr(tweet,"retweeted_status"):
        a = 1
        # print("----- Retweet ----")
        re.sub('(?<=[.])(?=[^\s | ^.])',text," ")
        try:
            text = tweet.extended_tweet["full_text"].replace("\n", " \n ").split(" ")[2:]

        except AttributeError:
            text = tweet.full_text.replace("\n", " \n ").split(" ")[2:]
        # print(text)
        sentence_list.append(text)

    else:
        # print("----- Non Retweet ----")
        try:
            text = tweet.extended_tweet["full_text"].replace("\n", " \n ").split(" ")
            # print(tweet.extended_tweet["full_text"].replace("\\n", " ").split(" "))
        except AttributeError:
            # print(tweet.full_text.replace("\\n", " ").split(" "))
            text = tweet.full_text.replace("\n", " \n ").split(" ")
        # print(text)
        sentence_list.append(text)
print(sentence_list)
filename = "entrepreneurship.pickle"
outfile = open(filename,'wb')
pickle.dump(sentence_list,outfile)
outfile.close()
# csvFile.close()
# np.savetxt("tweets.csv",text_list,delimiter=",",encoding="utf-8")
    # if not tweet.retweeted and ('RT @' not in tweet.text):
    #     print(tweet.text)
    #     print("======================")
