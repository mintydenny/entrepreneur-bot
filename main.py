import tweepy as tp
import mykeys as mk
import re
import numpy as np
import csv
import unicodedata
auth = tp.AppAuthHandler(mk.CONSUMER_KEY,mk.CONSUMER_SECRET)
api = tp.API(auth)
text_list=[]
csvFile = open("tweets5.csv","a")
csvWriter = csv.writer(csvFile)

# Get tweets with #entrepreneurlife
for tweet in tp.Cursor(api.search,q='#entrepreneurlife',lang="en",result_type="mixed",tweet_mode="extended").items(50):
    text = ""
    if hasattr(tweet,"retweeted_status"):
        a = 1
        # print("----- Retweet ----")
        # re.sub('(?<=[.])(?=[^\s | ^.])',text," ")
        # try:
            # print(tweet.extended_tweet["full_text"].replace("\\n", " ").split(" ")[2:])
        # except AttributeError:
            # print(tweet.full_text.replace("\\n", " ").split(" ")[2:])
    else:
        # print("----- Non Retweet ----")
        try:
            text = tweet.extended_tweet["full_text"].replace("\\n", " ").encode("utf8").split(" ")
            # print(tweet.extended_tweet["full_text"].replace("\\n", " ").split(" "))
        except AttributeError:
            # print(tweet.full_text.replace("\\n", " ").split(" "))
            text = tweet.full_text.replace("\\n", " ").encode("utf8").split(" ")
            a=1
        csvWriter.writerow([text])

markov_model = {}

# csvFile.close()
# np.savetxt("tweets.csv",text_list,delimiter=",",encoding="utf-8")
    # if not tweet.retweeted and ('RT @' not in tweet.text):
    #     print(tweet.text)
    #     print("======================")
