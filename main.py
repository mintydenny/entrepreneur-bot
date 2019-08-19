import tweepy as tp
import mykeys as mk


auth = tp.AppAuthHandler(mk.CONSUMER_KEY,mk.CONSUMER_SECRET)
api = tp.API(auth)
for tweet in tp.Cursor(api.search,q='#entrepreneurlife',lang="en",result_type="mixed",tweet_mode="extended").items(10):
    if hasattr(tweet,"retweeted_status"):
        print("----- Retweet ----")
        try:
            print(tweet.extended_tweet["full_text"])
        except AttributeError:
            print(tweet.full_text)
    else:
        print("----- Non Retweet ----")
        try:
            print(tweet.extended_tweet["full_text"])
        except AttributeError:
            print(tweet.full_text)
    print("===============")
    # if not tweet.retweeted and ('RT @' not in tweet.text):
    #     print(tweet.text)
    #     print("======================")
